"""
Sheet reader implementations for Excel and Google Sheets.
"""

import logging
import os
import pickle
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

import gspread
import pandas as pd

try:
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from google.oauth2.service_account import Credentials
except ImportError:
    InstalledAppFlow = None
    Request = None
    Credentials = None

try:
    from scripts.helpers.config import normalize_column_name
    from .utils import get_iso_timestamp
except ImportError:
    from config import normalize_column_name
    from utils import get_iso_timestamp

logger = logging.getLogger(__name__)


class BaseSheetReader(ABC):
    """Abstract base class for sheet readers."""

    @abstractmethod
    def read(self) -> List[Dict[str, Any]]:
        """
        Read sheet data.

        Returns:
            List of dictionaries, one per row
        """
        pass


class ExcelReader(BaseSheetReader):
    """Read data from Excel files."""

    def __init__(self, file_path: str):
        """
        Initialize Excel reader.

        Args:
            file_path: Path to Excel file (.xlsx or .xls)
        """
        self.file_path = file_path

    def read(self) -> List[Dict[str, Any]]:
        """
        Read Excel file and return list of row dictionaries.

        Returns:
            List of dictionaries with column names as keys
        """
        logger.info(f"Reading Excel file: {self.file_path}")

        try:
            # Check file extension and read accordingly
            if self.file_path.endswith('.csv'):
                df = pd.read_csv(self.file_path, dtype=str)
            else:
                # Read Excel file (.xlsx, .xls)
                df = pd.read_excel(self.file_path, dtype=str)

            # Remove completely empty rows
            df = df.dropna(how='all')

            # Normalize column names for consistency
            original_columns = df.columns.tolist()
            logger.info(f"Found columns: {original_columns}")

            # Convert to list of dictionaries
            records = df.to_dict('records')

            logger.info(f"Read {len(records)} records from Excel file")
            return records

        except Exception as e:
            logger.error(f"Error reading Excel file: {e}")
            raise


class GoogleSheetsReader(BaseSheetReader):
    """Read data from Google Sheets."""

    def __init__(
        self,
        spreadsheet_url: str,
        sheet_name: str = "Demande d'adhésion",
        auth_method: str = "oauth2",
        credentials_path: Optional[str] = None
    ):
        """
        Initialize Google Sheets reader.

        Args:
            spreadsheet_url: URL or ID of the Google Spreadsheet
            sheet_name: Name of the worksheet to read
            auth_method: Authentication method ('oauth2' or 'service-account')
            credentials_path: Path to credentials file
        """
        self.spreadsheet_url = spreadsheet_url
        self.sheet_name = sheet_name
        self.auth_method = auth_method
        self.credentials_path = credentials_path
        self.client = None

    def _authenticate_oauth2(self) -> 'gspread.Client':
        """
        Authenticate using OAuth2 flow.

        Returns:
            Authenticated gspread client
        """
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

        creds = None
        token_file = 'token.pickle'

        # Try to load saved credentials
        if os.path.exists(token_file):
            with open(token_file, 'rb') as token:
                creds = pickle.load(token)

        # If no valid credentials, do OAuth2 flow
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not self.credentials_path:
                    raise ValueError("OAuth2 requires credentials_path to credentials.json")

                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_path, SCOPES
                )
                creds = flow.run_local_server(port=0)

            # Save credentials for next run
            with open(token_file, 'wb') as token:
                pickle.dump(creds, token)

        return gspread.authorize(creds)

    def _authenticate_service_account(self) -> 'gspread.Client':
        """
        Authenticate using service account.

        Returns:
            Authenticated gspread client
        """
        if not self.credentials_path:
            raise ValueError("Service account requires credentials_path to service account JSON")

        SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

        creds = Credentials.from_service_account_file(
            self.credentials_path,
            scopes=SCOPES
        )

        return gspread.authorize(creds)

    def _authenticate(self) -> 'gspread.Client':
        """
        Authenticate based on configured method.

        Returns:
            Authenticated gspread client
        """
        if self.auth_method == 'oauth2':
            return self._authenticate_oauth2()
        elif self.auth_method == 'service-account':
            return self._authenticate_service_account()
        else:
            raise ValueError(f"Unknown auth method: {self.auth_method}")

    def read(self) -> List[Dict[str, Any]]:
        """
        Read Google Sheet and return list of row dictionaries.

        Returns:
            List of dictionaries with column names as keys
        """
        logger.info(f"Reading Google Sheet: {self.spreadsheet_url}, worksheet: {self.sheet_name}")

        try:
            # Authenticate
            if not self.client:
                self.client = self._authenticate()

            # Open spreadsheet
            if self.spreadsheet_url.startswith('http'):
                spreadsheet = self.client.open_by_url(self.spreadsheet_url)
            else:
                spreadsheet = self.client.open_by_key(self.spreadsheet_url)

            # Get worksheet
            worksheet = spreadsheet.worksheet(self.sheet_name)

            # Get all records as list of dictionaries
            records = worksheet.get_all_records()

            # Remove empty rows
            records = [r for r in records if any(v for v in r.values())]

            logger.info(f"Read {len(records)} records from Google Sheet")
            return records

        except Exception as e:
            logger.error(f"Error reading Google Sheet: {e}")
            raise


class SheetWriter:
    """Write data to Excel sheets."""

    @staticmethod
    def write_failed_records(
        failed_records: List[Dict[str, Any]],
        output_path: str
    ) -> None:
        """
        Write failed records to an Excel or CSV file.
        File format is determined by the file extension (.xlsx, .xls, .csv)

        Args:
            failed_records: List of dictionaries with failed record data
            output_path: Path to output file (.xlsx, .xls, or .csv)
        """
        if not failed_records:
            logger.info("No failed records to write")
            return

        logger.info(f"Writing {len(failed_records)} failed records to {output_path}")

        try:
            # Convert to DataFrame
            df = pd.DataFrame(failed_records)

            # Ensure error columns are at the end
            error_cols = ['error_reason', 'error_timestamp']
            other_cols = [col for col in df.columns if col not in error_cols]
            df = df[other_cols + [col for col in error_cols if col in df.columns]]

            # Write based on file extension
            if output_path.endswith('.csv'):
                # Write to CSV
                df.to_csv(output_path, index=False, encoding='utf-8')
            else:
                # Write to Excel (.xlsx, .xls)
                df.to_excel(output_path, index=False, engine='openpyxl')

            logger.info(f"Successfully wrote failed records to {output_path}")

        except Exception as e:
            logger.error(f"Error writing failed records: {e}")
            raise
