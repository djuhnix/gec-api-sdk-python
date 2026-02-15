#!/usr/bin/env python3
"""
CLI script for importing member data from Excel or Google Sheets.

Usage:
    python import_members.py --source excel --input data.xlsx
    python import_members.py --source gsheet --input https://docs.google.com/spreadsheets/d/... --auth-method oauth2
"""

import argparse
import logging
import sys

# Handle imports whether running as script or module
try:
    from scripts.helpers.config import get_column_map
    from scripts.helpers.member_importer import MemberImporter
    from scripts.helpers.sheet_reader import ExcelReader, GoogleSheetsReader
    from scripts.helpers.utils import (
        setup_logging,
        load_env_variables,
        format_summary_table,
        get_timestamp,
        validate_file_path,
        anonymize_record
    )
except ImportError:
    from scripts.helpers.config import get_column_map
    from scripts.helpers.member_importer import MemberImporter
    from scripts.helpers.sheet_reader import ExcelReader, GoogleSheetsReader
    from scripts.helpers.utils import (
        setup_logging,
        load_env_variables,
        format_summary_table,
        get_timestamp,
        validate_file_path,
        anonymize_record
    )

logger = logging.getLogger(__name__)


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Import member data from Excel or Google Sheets to GEC API',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Import from Excel file
  python import_members.py --source excel --input members.xlsx
  
  # Import from Google Sheets with OAuth2
  python import_members.py --source gsheet --input "https://docs.google.com/spreadsheets/d/ABC123" \\
      --auth-method oauth2 --credentials-path credentials.json
  
  # Import with custom API settings
  python import_members.py --source excel --input data.xlsx \\
      --api-host https://api.example.com --api-token YOUR_TOKEN
  
  # Dry run (validate without creating)
  python import_members.py --source excel --input data.xlsx --dry-run
  
  # Stop on first error (useful for debugging)
  python import_members.py --source excel --input data.xlsx --stop-on-error
        '''
    )

    # Required arguments
    parser.add_argument(
        '--source',
        required=True,
        choices=['excel', 'gsheet'],
        help='Source type: excel or gsheet'
    )
    parser.add_argument(
        '--input',
        required=True,
        help='Input file path (for excel) or spreadsheet URL/ID (for gsheet)'
    )

    # Optional arguments
    parser.add_argument(
        '--sheet-name',
        default="Demande d'adhésion",
        help='Worksheet name for Google Sheets (default: "Demande d\'adhésion")'
    )
    parser.add_argument(
        '--output-failed',
        help='Output path for failed records (default: failed_imports_TIMESTAMP.xlsx or .csv)'
    )
    parser.add_argument(
        '--output-format',
        choices=['excel', 'csv'],
        default='excel',
        help='Output format for failed records: excel (.xlsx) or csv (default: excel)'
    )
    parser.add_argument(
        '--api-host',
        help='API host URL (default: from GEC_API_HOST env var)'
    )
    parser.add_argument(
        '--api-token',
        help='API JWT token (default: from GEC_API_TOKEN env var)'
    )
    parser.add_argument(
        '--auth-method',
        choices=['oauth2', 'service-account'],
        default='oauth2',
        help='Google Sheets authentication method (default: oauth2)'
    )
    parser.add_argument(
        '--credentials-path',
        help='Path to Google credentials file (default: from GOOGLE_CREDENTIALS_PATH env var)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Validate data without creating members'
    )
    parser.add_argument(
        '--anonymize',
        action='store_true',
        help='Anonymize sensitive data (names, emails, phones, addresses) before processing'
    )
    parser.add_argument(
        '--stop-on-error',
        action='store_true',
        help='Stop importing immediately after the first failed record (useful for debugging)'
    )
    parser.add_argument(
        '--batch-size',
        type=int,
        default=50,
        help='Number of records to process per batch (default: 50)'
    )
    parser.add_argument(
        '--log-level',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        default='INFO',
        help='Logging level (default: INFO)'
    )

    return parser.parse_args()


def main():
    """Main entry point."""
    # Parse arguments
    args = parse_arguments()

    # Setup logging
    setup_logging(args.log_level)
    logger.info("Starting member import process")

    try:
        # Load environment variables
        env_vars = load_env_variables()

        # Get API configuration
        api_host = args.api_host or env_vars['api_host']
        api_token = args.api_token or env_vars['api_token']

        if not api_token and not args.dry_run:
            logger.error("API token is required. Set GEC_API_TOKEN env var or use --api-token")
            return 2

        # Get credentials path for Google Sheets
        credentials_path = args.credentials_path or env_vars['google_credentials_path']

        # Validate input
        if args.source == 'excel':
            if not validate_file_path(args.input):
                logger.error(f"Input file not found or not readable: {args.input}")
                return 2

        # Get column mapping for source type
        column_map = get_column_map(args.source)

        # Create reader based on source type
        if args.source == 'excel':
            logger.info(f"Reading from Excel file: {args.input}")
            reader = ExcelReader(args.input)
        else:  # gsheet
            logger.info(f"Reading from Google Sheets: {args.input}")
            if not credentials_path and not args.dry_run:
                logger.error("Google Sheets requires credentials. Set GOOGLE_CREDENTIALS_PATH env var or use --credentials-path")
                return 2

            reader = GoogleSheetsReader(
                spreadsheet_url=args.input,
                sheet_name=args.sheet_name,
                auth_method=args.auth_method,
                credentials_path=credentials_path
            )

        # Read records
        try:
            records = reader.read()
        except Exception as e:
            logger.error(f"Error reading input: {e}")
            return 2

        if not records:
            logger.warning("No records found in input")
            return 0

        logger.info(f"Found {len(records)} records to process")

        # Anonymize data if requested
        if args.anonymize:
            logger.info("Anonymizing sensitive data...")
            records = [anonymize_record(record) for record in records]
            logger.info(f"Anonymized {len(records)} records")

        # Create importer
        importer = MemberImporter(
            api_host=api_host,
            api_token=api_token,
            source_type=args.source,
            column_map=column_map
        )

        # Import members
        success_records, failed_records, duplicate_records = importer.import_members(
            records=records,
            dry_run=args.dry_run,
            batch_size=args.batch_size
        )

        # Generate output path for failed records
        output_failed_path = args.output_failed
        if not output_failed_path and failed_records:
            # Use format from args.output_format
            extension = 'csv' if args.output_format == 'csv' else 'xlsx'
            output_failed_path = f"failed_imports_{get_timestamp()}.{extension}"

        # Generate report
        summary = importer.generate_report(
            success_records=success_records,
            failed_records=failed_records,
            duplicate_records=duplicate_records,
            output_failed_path=output_failed_path
        )

        # Print summary
        print("\n" + format_summary_table(summary))

        # Show some examples of failures if any
        if failed_records:
            print("\nSample failed records:")
            for i, record in enumerate(failed_records[:3], 1):
                email = record['original_data'].get('email', 'N/A')
                reason = record.get('error_reason', 'Unknown')
                print(f"  {i}. Row {record['row_index']}, Email: {email}")
                print(f"     Error: {reason}")

            if len(failed_records) > 3:
                print(f"  ... and {len(failed_records) - 3} more")

        # Show some examples of duplicates if any
        if duplicate_records:
            print("\nSample duplicate records:")
            for i, record in enumerate(duplicate_records[:3], 1):
                email = record['original_data'].get('email', 'N/A')
                print(f"  {i}. Row {record['row_index']}, Email: {email}")

            if len(duplicate_records) > 3:
                print(f"  ... and {len(duplicate_records) - 3} more")

        # Determine exit code
        if args.dry_run:
            logger.info("Dry run complete - no members were created")
            return 0

        if failed_records and not success_records:
            logger.error("All records failed")
            return 2
        elif failed_records:
            logger.warning("Some records failed")
            return 1
        else:
            logger.info("All records processed successfully")
            return 0

    except KeyboardInterrupt:
        logger.info("Import cancelled by user")
        return 130

    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        return 2


if __name__ == '__main__':
    sys.exit(main())


