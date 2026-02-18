"""
Main orchestrator for member import process.
"""

import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, List, Any, Optional, Tuple

import gec_api_sdk
from gec_api_sdk.rest import ApiException

try:
    from .data_processor import MemberDataProcessor
    from scripts.helpers.duplicate_checker import DuplicateChecker
    from .sheet_reader import SheetWriter
    from .utils import get_iso_timestamp
except ImportError:
    from data_processor import MemberDataProcessor
    from duplicate_checker import DuplicateChecker
    from sheet_reader import SheetWriter
    from utils import get_iso_timestamp

logger = logging.getLogger(__name__)


class MemberImporter:
    """Orchestrate the member import process."""

    def __init__(
        self,
        api_host: str,
        api_token: str,
        source_type: str,
        column_map: Dict[str, str]
    ):
        """
        Initialize the member importer.

        Args:
            api_host: API host URL
            api_token: JWT bearer token
            source_type: Type of source ('excel' or 'gsheet')
            column_map: Column mapping dictionary
        """
        self.api_host = api_host
        self.api_token = api_token
        self.source_type = source_type

        # Configure SDK
        self.configuration = gec_api_sdk.Configuration(
            host=api_host,
            access_token=api_token
        )

        # Create API client and member API
        self.api_client = gec_api_sdk.ApiClient(self.configuration)
        self.member_api = gec_api_sdk.MemberApi(self.api_client)

        # Create helper instances
        self.data_processor = MemberDataProcessor(column_map)
        self.duplicate_checker = DuplicateChecker(self.api_client, self.member_api)

        # Counters
        self.reset_counters()

    def reset_counters(self) -> None:
        """Reset import counters."""
        self.total_count = 0
        self.success_count = 0
        self.failed_count = 0
        self.duplicate_count = 0
        self.skipped_count = 0
        self.not_processed_count = 0

    def import_members(
        self,
        records: List[Dict[str, Any]],
        dry_run: bool = False,
        batch_size: int = 50,
        stop_on_error: bool = False,
        concurrency: int = 10,
    ) -> Tuple[List[Dict], List[Dict], List[Dict]]:
        """
        Import member records.

        Records are processed in two phases per batch:
        1. Preparation (sequential): transform, validate, duplicate check.
        2. Creation (parallel): API calls fired concurrently up to `concurrency` workers.

        Args:
            records: List of record dictionaries from source
            dry_run: If True, don't actually create members
            batch_size: Number of records to prepare per batch before firing API calls
            stop_on_error: If True, stop immediately after the first failure
            concurrency: Maximum number of parallel API creation calls

        Returns:
            Tuple of (success_records, failed_records, duplicate_records)
        """
        logger.info(
            f"Starting import of {len(records)} records "
            f"(dry_run={dry_run}, stop_on_error={stop_on_error}, concurrency={concurrency})"
        )

        self.reset_counters()
        self.total_count = len(records)

        if not dry_run:
            self.duplicate_checker.load_existing_members()

        success_records: List[Dict] = []
        failed_records: List[Dict] = []
        duplicate_records: List[Dict] = []

        for batch_start in range(0, len(records), batch_size):
            batch = records[batch_start:batch_start + batch_size]
            batch_num = batch_start // batch_size + 1
            total_batches = (len(records) + batch_size - 1) // batch_size
            logger.info(
                f"Processing batch {batch_num}/{total_batches} "
                f"(records {batch_start + 1}-{min(batch_start + batch_size, len(records))})"
            )

            # ── Phase 1: sequential preparation ─────────────────────────────
            # Transform, validate, and duplicate-check each record in order.
            # Records that pass become "ready" payloads for Phase 2.
            prepared: List[Dict] = []
            should_stop = False

            for idx, record in enumerate(batch, start=batch_start):
                result = self._prepare_record(record, idx + 1)
                prepared.append(result)

                if result['status'] in ('failed', 'duplicate'):
                    if result['status'] == 'failed':
                        failed_records.append(result)
                        self.failed_count += 1
                        logger.warning(f"Row {idx + 1}: Validation failed - {result['error_reason']}")
                    else:
                        duplicate_records.append(result)
                        self.duplicate_count += 1
                        logger.info(f"Row {idx + 1}: Skipping duplicate - {result.get('member_email')}")

                    if stop_on_error and result['status'] == 'failed':
                        logger.warning("=" * 70)
                        logger.warning(f"⚠️  STOP ON ERROR TRIGGERED AT ROW {idx + 1}")
                        logger.warning(f"Error reason: {result.get('error_reason', 'Unknown')}")
                        logger.warning(
                            f"Import stopped: {self.success_count} success, "
                            f"{self.failed_count} failed, {self.duplicate_count} duplicates"
                        )
                        logger.warning("=" * 70)
                        should_stop = True
                        break

            if should_stop:
                # Option A: flush records already validated in this batch before stopping.
                # This preserves work done so far and avoids silently losing records.
                ready = [r for r in prepared if r['status'] == 'ready']
                self._run_phase2(ready, dry_run, concurrency, success_records, failed_records)

                # Add remaining unprocessed records to failed_records with a clear reason
                current_batch_end = batch_start + len(prepared)
                stop_row = prepared[-1]['row_index']
                self._append_not_processed(
                    records[current_batch_end:], current_batch_end, stop_row, failed_records
                )

                logger.warning("=" * 70)
                logger.warning(f"⚠️  STOP ON ERROR TRIGGERED AT ROW {stop_row}")
                logger.warning(f"Error reason: {prepared[-1].get('error_reason', 'Unknown')}")
                logger.warning(
                    f"Import stopped: {self.success_count} success, "
                    f"{self.failed_count} failed, {self.duplicate_count} duplicates"
                )
                if self.not_processed_count > 0:
                    logger.warning(
                        f"Not processed (remaining rows): {self.not_processed_count} record(s) "
                        f"(rows {current_batch_end + 1}–{len(records)}) — re-run from that offset to continue"
                    )
                logger.warning("=" * 70)
                return success_records, failed_records, duplicate_records

            # ── Phase 2: parallel API creation ──────────────────────────────
            # Fire all "ready" creation calls concurrently; dry-run records are
            # resolved immediately without touching the API.
            ready = [r for r in prepared if r['status'] == 'ready']
            stop_triggered = self._run_phase2(ready, dry_run, concurrency, success_records, failed_records)

            if stop_triggered and stop_on_error:
                # Add all records from subsequent batches to failed_records
                next_batch_start = batch_start + batch_size
                stop_row = next((r['row_index'] for r in failed_records[-1:]), '?')
                self._append_not_processed(
                    records[next_batch_start:], next_batch_start, stop_row, failed_records
                )
                if self.not_processed_count > 0:
                    next_row = next_batch_start + 1
                    logger.warning(
                        f"Not processed (remaining rows): {self.not_processed_count} record(s) "
                        f"(rows {next_row}–{len(records)}) — re-run from that offset to continue"
                    )
                return success_records, failed_records, duplicate_records

        logger.info(
            f"Import complete: {self.success_count} success, "
            f"{self.failed_count} failed, {self.duplicate_count} duplicates"
        )
        return success_records, failed_records, duplicate_records

    def _run_phase2(
        self,
        ready: List[Dict],
        dry_run: bool,
        concurrency: int,
        success_records: List[Dict],
        failed_records: List[Dict],
    ) -> bool:
        """
        Execute API creation calls for a list of validated records.

        Args:
            ready: Records with status 'ready' from Phase 1
            dry_run: If True, simulate without API calls
            concurrency: Max parallel workers
            success_records: Accumulator list for successes (mutated in place)
            failed_records: Accumulator list for failures (mutated in place)

        Returns:
            True if a stop-on-error condition was hit (API failure), False otherwise
        """
        if not ready:
            return False

        if dry_run:
            for result in ready:
                email = result.get('member_email')
                doc_msg = f" (would attach {len(result['_documents'])} document(s))" if result['_documents'] else ""
                logger.info(f"Row {result['row_index']}: [DRY RUN] Would create member - {email}{doc_msg}")
                result['status'] = 'success'
                success_records.append(result)
                self.success_count += 1
            return False

        with ThreadPoolExecutor(max_workers=concurrency) as executor:
            futures = {
                executor.submit(self._create_member, r['_member_data'], r['_documents']): r
                for r in ready
            }
            for future in as_completed(futures):
                result = futures[future]
                try:
                    created_member = future.result()
                    result['status'] = 'success'
                    result['member_id'] = getattr(created_member, 'id', None)
                    result['member_email'] = getattr(created_member, 'email', None)
                    result['error_reason'] = None
                    self.success_count += 1
                    doc_msg = f" with {len(result['_documents'])} document(s)" if result['_documents'] else ""
                    logger.info(
                        f"Row {result['row_index']}: Successfully created member"
                        f" - {result.get('member_email')}{doc_msg}"
                    )
                except gec_api_sdk.ApiException as e:
                    result['status'] = 'failed'
                    result['error_reason'] = f"API error ({e.status}): {e.body if e.body else str(e)}"
                    self.failed_count += 1
                    logger.error(
                        f"Row {result['row_index']}: API error ({e.status})"
                        f" - {e.body if e.body else str(e)}"
                    )
                except Exception as e:
                    result['status'] = 'failed'
                    result['error_reason'] = f"Unexpected error: {str(e)}"
                    self.failed_count += 1
                    logger.error(f"Row {result['row_index']}: Unexpected error - {str(e)}", exc_info=True)

                if result['status'] == 'success':
                    success_records.append(result)
                else:
                    failed_records.append(result)
                    # Signal caller to stop; cancel pending futures
                    for f in futures:
                        f.cancel()
                    return True

        return False

    def _append_not_processed(
        self,
        remaining_records: List[Dict],
        start_index: int,
        stop_row: int,
        failed_records: List[Dict],
    ) -> None:
        """
        Add records that were never reached (due to stop-on-error) to failed_records.

        Args:
            remaining_records: Source records that were not processed
            start_index: 0-based index of the first remaining record in the full list
            stop_row: Row number that triggered the stop (for the error message)
            failed_records: Accumulator list (mutated in place)
        """
        reason = f"Not processed: import stopped due to error at row {stop_row}"
        for offset, record in enumerate(remaining_records):
            row_index = start_index + offset + 1
            failed_records.append({
                'row_index': row_index,
                'status': 'failed',
                'original_data': record.copy(),
                'error_reason': reason,
                'error_timestamp': get_iso_timestamp(),
                '_member_data': None,
                '_documents': [],
            })
            self.failed_count += 1
        self.not_processed_count = len(remaining_records)

    def _prepare_record(
        self,
        record: Dict[str, Any],
        row_index: int,
    ) -> Dict[str, Any]:
        """
        Transform, validate, and duplicate-check a single record (no API call).

        Returns a result dict with status 'ready', 'failed', or 'duplicate'.
        Ready results carry '_member_data' and '_documents' for Phase 2.
        """
        result: Dict[str, Any] = {
            'row_index': row_index,
            'status': 'failed',
            'original_data': record.copy(),
            'error_reason': None,
            'error_timestamp': get_iso_timestamp(),
            '_member_data': None,
            '_documents': [],
        }

        try:
            transformed_data, field_errors, documents = self.data_processor.transform_row(record)
            transformed_data = self.data_processor.apply_defaults(transformed_data)
            is_valid, validation_errors = self.data_processor.validate_member(transformed_data)

            all_errors = [f"Field {k}: {v}" for k, v in field_errors.items()] + validation_errors
            if all_errors:
                result['error_reason'] = "; ".join(all_errors)
                return result

            # Duplicate check (in-memory, safe to run sequentially)
            email = transformed_data.get('email')
            result['member_email'] = email
            if email and self.duplicate_checker.is_duplicate(email, dry_run=False):
                duplicate_info = self.duplicate_checker.get_duplicate_info(email)
                result['status'] = 'duplicate'
                result['error_reason'] = (
                    f"Duplicate email: {email} (existing member ID: {duplicate_info.get('id')})"
                )
                return result

            result['status'] = 'ready'
            result['_member_data'] = transformed_data
            result['_documents'] = documents

        except Exception as e:
            result['error_reason'] = f"Unexpected error during preparation: {str(e)}"
            logger.error(f"Row {row_index}: Unexpected error - {str(e)}", exc_info=True)

        return result

    def _create_member(self, member_data: Dict[str, Any], documents: List[Dict[str, str]] = None) -> Any:
        """
        Create a member via API and attach any documents.

        Args:
            member_data: Member data dictionary
            documents: List of documents to attach to the member

        Returns:
            Created member object

        Raises:
            ApiException: If API call fails
        """
        try:
            # Log the request data for debugging
            logger.debug(f"Creating member with data: {member_data}")

            # Create Pydantic model from dictionary
            # The API expects a MemberMemberWrite object, not a dict
            member_model = gec_api_sdk.MemberMemberWrite(**member_data)
            logger.debug(f"Created Pydantic model: {member_model.model_dump(by_alias=True)}")

            # Call API to create member with correct parameter name
            # NOTE: The parameter is 'member_member_write', NOT 'body'
            created_member = self.member_api.api_members_post(member_member_write=member_model)

            logger.info(f"Successfully created member in API: {getattr(created_member, 'id', 'unknown')}")

            # If there are documents and member was created successfully, create documents
            if documents and created_member:
                member_id = getattr(created_member, 'id', None)
                if member_id:
                    self._create_member_documents(member_id, documents)

            return created_member

        except gec_api_sdk.ApiException as e:
            logger.error(f"API error creating member: {e}")
            logger.error(f"API response status: {e.status}")
            logger.error(f"API response body: {e.body}")
            logger.error(f"API response headers: {e.headers}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error creating member: {e}")
            logger.error(f"Member data that caused error: {member_data}")
            raise

    def _create_member_documents(self, member_id: str, documents: List[Dict[str, str]]) -> None:
        """
        Create documents for a member.

        Args:
            member_id: ID of the member
            documents: List of document dictionaries with 'type', 'url', 'field'
        """
        document_api = gec_api_sdk.DocumentApi(self.api_client)

        for doc in documents:
            try:
                document_data = {
                    'type': doc['type'],
                    'url': doc['url'],
                    'member': f'/api/members/{member_id}'  # IRI reference to member
                }
                created_doc = document_api.api_documents_post(body=document_data)
                logger.info(f"Created document {doc['type']} for member {member_id}: {doc['url']}")
            except Exception as e:
                logger.warning(f"Failed to create document {doc['type']} for member {member_id}: {e}")

    def generate_report(
        self,
        success_records: List[Dict],
        failed_records: List[Dict],
        duplicate_records: List[Dict],
        output_failed_path: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Generate import summary report and save failed records.

        Args:
            success_records: List of successful imports
            failed_records: List of failed imports
            duplicate_records: List of duplicate records
            output_failed_path: Path to save failed records (if provided)

        Returns:
            Summary dictionary
        """
        summary = {
            'total': self.total_count,
            'success': self.success_count,
            'failed': self.failed_count,
            'duplicates': self.duplicate_count,
            'skipped': self.skipped_count,
            'not_processed': self.not_processed_count,
            'failed_file': None,
        }

        # Save failed records if any
        if failed_records and output_failed_path:
            try:
                # Prepare failed records for export (include original data + error info)
                export_records = []
                for record in failed_records:
                    export_row = record['original_data'].copy()
                    export_row['error_reason'] = record.get('error_reason', 'Unknown error')
                    export_row['error_timestamp'] = record.get('error_timestamp', get_iso_timestamp())
                    export_records.append(export_row)

                SheetWriter.write_failed_records(export_records, output_failed_path)
                summary['failed_file'] = output_failed_path
                logger.info(f"Saved {len(failed_records)} failed records to {output_failed_path}")

            except Exception as e:
                logger.error(f"Error saving failed records: {e}")

        return summary


