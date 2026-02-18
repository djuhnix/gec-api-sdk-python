"""
Data processor for cleaning and transforming member data.
"""

import logging
import math
import re
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Any

try:
    import numpy as np
    import pandas as pd
    _PANDAS_AVAILABLE = True
except ImportError:
    _PANDAS_AVAILABLE = False

try:
    from scripts.helpers.config import (
        GENDER_MAP, BOOLEAN_MAP, STATUS_MAP, MEMBERSHIP_TYPE_MAP,
        TRAINING_CYCLE_MAP, STUDY_LEVEL_MAP, CONTRIBUTION_STATUS_MAP,
        DATE_FORMATS, GENDER_VALUES, STATUS_VALUES, MEMBERSHIP_TYPE_VALUES,
        CONTRIBUTION_STATUS_VALUES,
        DEFAULT_STATUS, DEFAULT_MEMBERSHIP_TYPE, DEFAULT_CONTRIBUTION_STATUS, normalize_column_name
    )
except ImportError:
    from config import (
        GENDER_MAP, BOOLEAN_MAP, STATUS_MAP, MEMBERSHIP_TYPE_MAP,
        TRAINING_CYCLE_MAP, STUDY_LEVEL_MAP, CONTRIBUTION_STATUS_MAP,
        DATE_FORMATS, GENDER_VALUES, STATUS_VALUES, MEMBERSHIP_TYPE_VALUES,
        CONTRIBUTION_STATUS_VALUES,
        DEFAULT_STATUS, DEFAULT_MEMBERSHIP_TYPE, DEFAULT_CONTRIBUTION_STATUS, normalize_column_name
    )

# String representations treated as empty/missing
_EMPTY_STRINGS = frozenset(('', 'nan', 'nat', 'none'))

# Dispatch table: api_field → (cleaner_method_name, use_none_check)
# use_none_check=True means store value when `cleaned is not None` (needed for booleans where False is valid)
_FIELD_CLEANERS: Dict[str, tuple] = {
    'birthDate':         ('clean_date', False),
    'phoneNumberFr':     ('clean_phone', False),
    'phoneNumberCg':     ('clean_phone', False),
    'gender':            ('clean_gender', False),
    'email':             ('clean_email', False),
    'status':            ('clean_status', False),
    'membershipType':    ('clean_membership_type', False),
    'trainingCycle':     ('clean_training_cycle', False),
    'studyLevel':        ('clean_study_level', False),
    'otherAssociations': ('clean_boolean', True),
}

# Document fields that may contain boolean values or URLs
_DOCUMENT_FIELDS = frozenset({'hasPassportCg', 'hasVisa', 'hasSchoolCertificate'})

logger = logging.getLogger(__name__)


class MemberDataProcessor:
    """Process and clean member data for import."""

    def __init__(self, column_map: Dict[str, str]):
        """
        Initialize the data processor.

        Args:
            column_map: Dictionary mapping source columns to API fields
        """
        self.column_map = column_map
        # Create normalized version of column map for case-insensitive matching
        self.normalized_map = {
            normalize_column_name(k): v
            for k, v in column_map.items()
        }

    def _match_column(self, df_column: str) -> Optional[str]:
        """
        Match a dataframe column to an API field using case-insensitive matching.

        Args:
            df_column: Column name from dataframe

        Returns:
            API field name or None if no match
        """
        normalized = normalize_column_name(df_column)
        return self.normalized_map.get(normalized)

    def _is_empty(self, value: Any) -> bool:
        """Return True if value should be treated as empty/missing (None, NaN, empty string)."""
        if value is None:
            return True
        if isinstance(value, float) and math.isnan(value):
            return True
        if _PANDAS_AVAILABLE:
            try:
                if pd.isna(value):
                    return True
            except (TypeError, ValueError):
                pass
        if isinstance(value, str):
            return value.strip().lower() in _EMPTY_STRINGS
        return False

    def _clean_enum(self, value: Any, enum_map: dict, enum_values, field_name: str) -> Tuple[Optional[str], Optional[str]]:
        """Clean and validate an enum field using a translation map and valid-values set."""
        if self._is_empty(value):
            return None, None
        str_val = str(value).lower().strip()
        if str_val in enum_map:
            return enum_map[str_val], None
        if str_val in enum_values:
            return str_val, None
        return None, f"Unknown {field_name} value: {value}"

    def _clean_mapped_text(self, value: Any, text_map: dict) -> Tuple[Optional[str], Optional[str]]:
        """Clean a text field, applying a translation map but keeping original value if not found."""
        if self._is_empty(value):
            return None, None
        str_val = str(value).lower().strip()
        if str_val in text_map:
            return text_map[str_val], None
        return str(value).strip(), None

    def clean_date(self, value: Any) -> Tuple[Optional[str], Optional[str]]:
        """
        Parse and clean date value.

        Args:
            value: Date value to parse

        Returns:
            Tuple of (ISO format date string or None, error message or None)
        """
        if self._is_empty(value):
            return None, None

        # If already a datetime object
        if isinstance(value, datetime):
            return value.strftime('%Y-%m-%d'), None

        # Convert to string
        date_str = str(value).strip()

        # Safety net for NaT string representation
        if date_str.lower() in _EMPTY_STRINGS:
            return None, None

        # Handle datetime strings with time component (e.g., "1993-06-13 00:00:00")
        # Extract just the date part if it contains a space
        if ' ' in date_str:
            date_str = date_str.split(' ')[0]

        # Try each date format
        for date_format in DATE_FORMATS:
            try:
                parsed_date = datetime.strptime(date_str, date_format)
                return parsed_date.strftime('%Y-%m-%d'), None
            except ValueError:
                continue

        return None, f"Unable to parse date: {date_str}"

    def clean_phone(self, value: Any) -> Tuple[Optional[str], Optional[str]]:
        """
        Clean and validate phone number.

        Args:
            value: Phone number to clean

        Returns:
            Tuple of (cleaned phone or None, error message or None)
        """
        if self._is_empty(value):
            return None, None

        # Convert to string and clean
        phone = str(value).strip()

        # Strip Unicode invisible/directional control characters (e.g. U+202A LTR embedding)
        phone = re.sub(r'[\u200b-\u200f\u202a-\u202e\u2066-\u2069\ufeff]', '', phone)

        # Remove common separators
        phone = phone.replace(' ', '').replace('-', '').replace('.', '').replace('(', '').replace(')', '')

        # Add + prefix if missing and starts with country code
        if not phone.startswith('+'):
            if phone.startswith('33'):
                phone = '+' + phone
            elif phone.startswith('242'):
                phone = '+' + phone
            elif phone.startswith('0') and len(phone) == 10:
                # French number starting with 0, convert to +33
                phone = '+33' + phone[1:]

        # Basic validation (should start with + and have numbers)
        if phone and not re.match(r'^\+\d{10,15}$', phone):
            return phone, f"Phone format may be invalid: {phone}"

        return phone if phone else None, None

    def clean_boolean(self, value: Any) -> Tuple[Optional[bool], Optional[str]]:
        """
        Convert value to boolean.

        Special handling for firstYear field:
        - If value is a year (e.g., "2026"), compare with current year
        - If value is boolean text (oui/non/yes/no), convert directly

        Special handling for NaN and empty values:
        - NaN, nan, None, empty string -> None

        Args:
            value: Value to convert

        Returns:
            Tuple of (boolean or None, error message or None)
        """
        if self._is_empty(value):
            return None, None

        # If already a boolean
        if isinstance(value, bool):
            return value, None

        # Convert to string and normalize
        str_value = str(value).lower().strip()

        # Check if it's a year value (4 digits)
        if str_value.isdigit() and len(str_value) == 4:
            try:
                year = int(str_value)
                current_year = datetime.now().year
                # Return True if the year matches current year
                return year == current_year, None
            except ValueError:
                pass

        # Check in boolean map
        if str_value in BOOLEAN_MAP:
            return BOOLEAN_MAP[str_value], None

        # Try to interpret as truthy/falsy
        if str_value in ['x', 'ok', 'checked']:
            return True, None

        return None, f"Unable to parse boolean: {value}"

    def clean_gender(self, value: Any) -> Tuple[Optional[str], Optional[str]]:
        """
        Clean and validate gender value.

        Args:
            value: Gender value to clean

        Returns:
            Tuple of (gender enum or None, error message or None)
        """
        return self._clean_enum(value, GENDER_MAP, GENDER_VALUES, 'gender')

    def clean_email(self, value: Any) -> Tuple[Optional[str], Optional[str]]:
        """
        Clean and validate email address.

        Args:
            value: Email to clean

        Returns:
            Tuple of (cleaned email or None, error message or None)
        """
        if self._is_empty(value):
            return None, None

        email = str(value).strip().lower()

        # Basic email validation
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            return None, f"Invalid email format: {email}"

        return email, None

    def clean_text(self, value: Any) -> Optional[str]:
        """
        Clean text value (strip whitespace, convert empty to None).

        Args:
            value: Text value to clean

        Returns:
            Cleaned text or None
        """
        if value is None:
            return None

        text = str(value).strip()
        return text if text else None

    def clean_status(self, value: Any) -> Tuple[Optional[str], Optional[str]]:
        """
        Clean and validate status value.

        Args:
            value: Status value to clean

        Returns:
            Tuple of (status enum or None, error message or None)
        """
        return self._clean_enum(value, STATUS_MAP, STATUS_VALUES, 'status')

    def clean_membership_type(self, value: Any) -> Tuple[Optional[str], Optional[str]]:
        """
        Clean and validate membership type value.

        Args:
            value: Membership type value to clean

        Returns:
            Tuple of (membership type enum or None, error message or None)
        """
        return self._clean_enum(value, MEMBERSHIP_TYPE_MAP, MEMBERSHIP_TYPE_VALUES, 'membership type')

    def clean_training_cycle(self, value: Any) -> Tuple[Optional[str], Optional[str]]:
        """
        Clean training cycle value.

        Args:
            value: Training cycle value to clean

        Returns:
            Tuple of (cleaned training cycle or None, error message or None)
        """
        return self._clean_mapped_text(value, TRAINING_CYCLE_MAP)

    def clean_study_level(self, value: Any) -> Tuple[Optional[str], Optional[str]]:
        """
        Clean study level value.

        Args:
            value: Study level value to clean

        Returns:
            Tuple of (cleaned study level or None, error message or None)
        """
        return self._clean_mapped_text(value, STUDY_LEVEL_MAP)

    def clean_document_field(self, value: Any, field_name: str = '') -> Tuple[Optional[bool], Optional[str], Optional[str]]:
        """
        Clean document-related boolean field (hasVisa, hasSchoolCertificate, hasPassportCg).

        Special handling:
        - If value is a URL, return (True, None, url) to indicate document exists with URL
        - If value is NaN/empty, return (None/False, None, None) depending on field
        - If value is boolean text, return (boolean, None, None)

        Args:
            value: Value to clean
            field_name: Name of the field for context

        Returns:
            Tuple of (boolean or None, error message or None, document_url or None)
        """
        default_value = False if 'visa' in field_name.lower() else None
        if self._is_empty(value):
            return default_value, None, None

        # If already a boolean
        if isinstance(value, bool):
            return value, None, None

        # Convert to string and normalize
        str_value = str(value).strip()

        # Check if it's a URL (contains http:// or https://)
        if str_value.startswith('http://') or str_value.startswith('https://'):
            # It's a URL - return True (document exists) and the URL
            return True, None, str_value

        # Check in boolean map
        str_value_lower = str_value.lower()
        if str_value_lower in BOOLEAN_MAP:
            return BOOLEAN_MAP[str_value_lower], None, None

        # Try to interpret as truthy/falsy
        if str_value_lower in ['x', 'ok', 'checked']:
            return True, None, None

        return None, f"Unable to parse boolean/document field: {value}", None

    def transform_row(self, row_dict: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, str], List[Dict[str, str]]]:
        """
        Transform a row from source format to API format.

        Special handling for firstYear:
        - Prefers 'is_first_year_study' column (boolean values like oui/non)
        - Falls back to 'first_year' column (year values) only if is_first_year_study not present

        Args:
            row_dict: Dictionary with source column names as keys

        Returns:
            Tuple of (transformed data dict, field errors dict, documents list)
        """
        transformed = {}
        field_errors = {}
        documents = []  # List of documents to create for this member

        # Check if we have is_first_year_study column for priority handling
        has_is_first_year_study = any(
            normalize_column_name(col) == normalize_column_name('is_first_year_study')
            for col in row_dict.keys()
        )

        # Map columns
        for source_col, value in row_dict.items():
            api_field = self._match_column(source_col)

            if api_field is None:
                continue  # Skip unmapped columns

            # isFirstYearStudy: prefer is_first_year_study (boolean) column over first_year (year value)
            if api_field == 'isFirstYearStudy':
                if normalize_column_name(source_col) == normalize_column_name('first_year') and has_is_first_year_study:
                    continue
                cleaned, error = self.clean_boolean(value)
                if error:
                    field_errors[api_field] = error
                if cleaned is not None:
                    transformed[api_field] = cleaned

            # Simple fields: look up cleaner in dispatch table
            elif api_field in _FIELD_CLEANERS:
                method_name, use_none_check = _FIELD_CLEANERS[api_field]
                cleaned, error = getattr(self, method_name)(value)
                if error:
                    field_errors[api_field] = error
                if (cleaned is not None) if use_none_check else cleaned:
                    transformed[api_field] = cleaned

            # Document fields (boolean + optional URL)
            elif api_field in _DOCUMENT_FIELDS:
                cleaned, error, document_url = self.clean_document_field(value, api_field)
                if error:
                    field_errors[api_field] = error
                if cleaned is not None:
                    transformed[api_field] = cleaned
                if document_url:
                    doc_type = api_field.replace('has', '')
                    documents.append({'type': doc_type, 'url': document_url, 'field': api_field})

            elif api_field == 'contribution':
                if self._is_empty(value):
                    continue
                str_value = str(value).strip()
                clean_num = str_value.replace('€', '').replace('$', '').replace(',', '.').strip()
                try:
                    amount = float(clean_num)
                    if not math.isnan(amount):
                        transformed['contribution'] = amount
                except (ValueError, AttributeError):
                    status_str = str_value.lower()
                    if status_str in CONTRIBUTION_STATUS_MAP:
                        transformed['contributionStatus'] = CONTRIBUTION_STATUS_MAP[status_str]
                    else:
                        transformed['contributionStatus'] = 'pending'

            elif api_field == 'contributionStatus':
                if self._is_empty(value):
                    continue
                status_str = str(value).lower().strip()
                if status_str in CONTRIBUTION_STATUS_MAP:
                    transformed[api_field] = CONTRIBUTION_STATUS_MAP[status_str]
                elif status_str in CONTRIBUTION_STATUS_VALUES:
                    transformed[api_field] = status_str
                else:
                    field_errors[api_field] = f"Unknown contribution status: {value}"

            else:
                # Generic text field
                if self._is_empty(value):
                    continue
                cleaned = self.clean_text(value)
                if cleaned:
                    transformed[api_field] = cleaned

        return transformed, field_errors, documents

    def apply_defaults(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Apply default values for missing required fields.

        Args:
            data: Member data dictionary

        Returns:
            Data with defaults applied
        """
        if not data.get('status'):
            data['status'] = DEFAULT_STATUS

        if not data.get('membershipType'):
            data['membershipType'] = DEFAULT_MEMBERSHIP_TYPE

        if not data.get('contributionStatus'):
            data['contributionStatus'] = DEFAULT_CONTRIBUTION_STATUS

        return data

    def validate_member(self, data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate member data against required fields and enum values.

        Args:
            data: Member data dictionary

        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = []

        # Check required fields
        required_fields = ['firstName', 'lastName', 'status', 'membershipType']
        for field in required_fields:
            if not data.get(field):
                errors.append(f"Missing required field: {field}")

        # Validate enum values
        if data.get('gender') and data['gender'] not in GENDER_VALUES:
            errors.append(f"Invalid gender value: {data['gender']}")

        if data.get('status') and data['status'] not in STATUS_VALUES:
            errors.append(f"Invalid status value: {data['status']}")

        if data.get('membershipType') and data['membershipType'] not in MEMBERSHIP_TYPE_VALUES:
            errors.append(f"Invalid membershipType value: {data['membershipType']}")

        return len(errors) == 0, errors
