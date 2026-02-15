"""
Main orchestrator for member import process.
"""

import logging
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

    def import_members(
        self,
        records: List[Dict[str, Any]],
        dry_run: bool = False,
        batch_size: int = 50,
        stop_on_error: bool = False
    ) -> Tuple[List[Dict], List[Dict], List[Dict]]:
        """
        Import member records.

        Args:
            records: List of record dictionaries from source
            dry_run: If True, don't actually create members
            batch_size: Number of records to process in each batch
            stop_on_error: If True, stop immediately after first failed record

        Returns:
            Tuple of (success_records, failed_records, duplicate_records)
        """
        logger.info(f"Starting import of {len(records)} records (dry_run={dry_run}, stop_on_error={stop_on_error})")

        self.reset_counters()
        self.total_count = len(records)

        # Load existing members for duplicate checking
        if not dry_run:
            self.duplicate_checker.load_existing_members()

        success_records = []
        failed_records = []
        duplicate_records = []

        # Process records in batches
        for i in range(0, len(records), batch_size):
            batch = records[i:i + batch_size]
            batch_num = i // batch_size + 1
            total_batches = (len(records) + batch_size - 1) // batch_size

            logger.info(f"Processing batch {batch_num}/{total_batches} (records {i+1}-{min(i+batch_size, len(records))})")

            for idx, record in enumerate(batch, start=i):
                result = self._process_record(record, idx + 1, dry_run)

                if result['status'] == 'success':
                    success_records.append(result)
                elif result['status'] == 'duplicate':
                    duplicate_records.append(result)
                else:  # failed
                    failed_records.append(result)

                    # Stop on first error if flag is set
                    if stop_on_error:
                        logger.warning("="*70)
                        logger.warning(f"⚠️  STOP ON ERROR TRIGGERED AT ROW {idx + 1}")
                        logger.warning(f"Error reason: {result.get('error_reason', 'Unknown')}")
                        logger.warning(f"Import stopped: {self.success_count} success, {self.failed_count} failed, {self.duplicate_count} duplicates")
                        logger.warning("="*70)
                        return success_records, failed_records, duplicate_records

        logger.info(f"Import complete: {self.success_count} success, {self.failed_count} failed, {self.duplicate_count} duplicates")

        return success_records, failed_records, duplicate_records

    def _process_record(
        self,
        record: Dict[str, Any],
        row_index: int,
        dry_run: bool
    ) -> Dict[str, Any]:
        """
        Process a single record.

        Args:
            record: Source record dictionary
            row_index: Row number (1-based)
            dry_run: If True, don't actually create member

        Returns:
            Result dictionary with status and details
        """
        result = {
            'row_index': row_index,
            'status': 'failed',
            'original_data': record.copy(),
            'error_reason': None,
            'error_timestamp': get_iso_timestamp(),
        }

        try:
            # Transform data
            transformed_data, field_errors, documents = self.data_processor.transform_row(record)

            # Apply defaults
            transformed_data = self.data_processor.apply_defaults(transformed_data)

            # Validate
            is_valid, validation_errors = self.data_processor.validate_member(transformed_data)

            # Collect all errors
            all_errors = []
            if field_errors:
                all_errors.extend([f"Field {k}: {v}" for k, v in field_errors.items()])
            if validation_errors:
                all_errors.extend(validation_errors)

            if all_errors:
                result['error_reason'] = "; ".join(all_errors)
                result['status'] = 'failed'
                self.failed_count += 1
                logger.warning(f"Row {row_index}: Validation failed - {result['error_reason']}")
                return result

            # Check for duplicates
            email = transformed_data.get('email')
            if email and self.duplicate_checker.is_duplicate(email, dry_run):
                duplicate_info = self.duplicate_checker.get_duplicate_info(email)
                result['status'] = 'duplicate'
                result['error_reason'] = f"Duplicate email: {email} (existing member ID: {duplicate_info.get('id')})"
                self.duplicate_count += 1
                logger.info(f"Row {row_index}: Skipping duplicate - {email}")
                return result

            # Create member (if not dry run)
            if not dry_run:
                created_member = self._create_member(transformed_data, documents)
                result['status'] = 'success'
                result['member_id'] = getattr(created_member, 'id', None)
                result['member_email'] = getattr(created_member, 'email', None)
                result['error_reason'] = None
                self.success_count += 1
                doc_msg = f" with {len(documents)} document(s)" if documents else ""
                logger.info(f"Row {row_index}: Successfully created member - {email}{doc_msg}")
            else:
                result['status'] = 'success'
                result['member_email'] = email
                result['error_reason'] = None
                self.success_count += 1
                doc_msg = f" (would attach {len(documents)} document(s))" if documents else ""
                logger.info(f"Row {row_index}: [DRY RUN] Would create member - {email}{doc_msg}")

        except gec_api_sdk.ApiException as e:
            result['status'] = 'failed'
            result['error_reason'] = f"API error ({e.status}): {e.body if e.body else str(e)}"
            self.failed_count += 1
            logger.error(f"Row {row_index}: API error ({e.status}) - {e.body if e.body else str(e)}")
            logger.debug(f"API error details: status={e.status}, headers={e.headers}")
        except Exception as e:
            result['status'] = 'failed'
            result['error_reason'] = f"Unexpected error: {str(e)}"
            self.failed_count += 1
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


