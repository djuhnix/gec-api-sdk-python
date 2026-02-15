"""
Data processor for cleaning and transforming member data.
"""

import logging
import re
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Any

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

    def clean_date(self, value: Any) -> Tuple[Optional[str], Optional[str]]:
        """
        Parse and clean date value.

        Args:
            value: Date value to parse

        Returns:
            Tuple of (ISO format date string or None, error message or None)
        """
        if value is None or (isinstance(value, str) and not value.strip()):
            return None, None

        # Handle pandas NaN and numpy NaN
        try:
            import pandas as pd
            import numpy as np
            if pd.isna(value) or (isinstance(value, float) and np.isnan(value)):
                return None, None
        except (ImportError, TypeError):
            pass

        # If already a datetime object
        if isinstance(value, datetime):
            return value.strftime('%Y-%m-%d'), None

        # Convert to string
        date_str = str(value).strip()
        
        # Check for NaN string representation
        if date_str.lower() in ('nan', 'nat', 'none', ''):
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
        if value is None or (isinstance(value, str) and not value.strip()):
            return None, None

        # Convert to string and clean
        phone = str(value).strip()

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
        if value is None:
            return None, None

        # If already a boolean
        if isinstance(value, bool):
            return value, None

        # Convert to string and normalize
        str_value = str(value).lower().strip()

        if not str_value:
            return None, None

        # Handle NaN values (pandas NaN becomes string 'nan')
        if str_value == 'nan':
            return None, None

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
        if value is None or (isinstance(value, str) and not value.strip()):
            return None, None

        gender_str = str(value).lower().strip()

        # Check in gender map
        if gender_str in GENDER_MAP:
            return GENDER_MAP[gender_str], None

        # Check if already a valid enum value
        if gender_str in GENDER_VALUES:
            return gender_str, None

        return None, f"Unknown gender value: {value}"

    def clean_email(self, value: Any) -> Tuple[Optional[str], Optional[str]]:
        """
        Clean and validate email address.

        Args:
            value: Email to clean

        Returns:
            Tuple of (cleaned email or None, error message or None)
        """
        if value is None or (isinstance(value, str) and not value.strip()):
            return None, "Email is required"

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
        if value is None or (isinstance(value, str) and not value.strip()):
            return None, None

        status_str = str(value).lower().strip()

        # Check in status map
        if status_str in STATUS_MAP:
            return STATUS_MAP[status_str], None

        # Check if already a valid enum value
        if status_str in STATUS_VALUES:
            return status_str, None

        return None, f"Unknown status value: {value}"

    def clean_membership_type(self, value: Any) -> Tuple[Optional[str], Optional[str]]:
        """
        Clean and validate membership type value.

        Args:
            value: Membership type value to clean

        Returns:
            Tuple of (membership type enum or None, error message or None)
        """
        if value is None or (isinstance(value, str) and not value.strip()):
            return None, None

        type_str = str(value).lower().strip()

        # Check in membership type map
        if type_str in MEMBERSHIP_TYPE_MAP:
            return MEMBERSHIP_TYPE_MAP[type_str], None

        # Check if already a valid enum value
        if type_str in MEMBERSHIP_TYPE_VALUES:
            return type_str, None

        return None, f"Unknown membership type: {value}"

    def clean_training_cycle(self, value: Any) -> Tuple[Optional[str], Optional[str]]:
        """
        Clean training cycle value.

        Args:
            value: Training cycle value to clean

        Returns:
            Tuple of (cleaned training cycle or None, error message or None)
        """
        if value is None or (isinstance(value, str) and not value.strip()):
            return None, None

        cycle_str = str(value).lower().strip()

        # Check in training cycle map
        if cycle_str in TRAINING_CYCLE_MAP:
            return TRAINING_CYCLE_MAP[cycle_str], None

        # Return as-is if not in map (keep original formatting)
        return str(value).strip(), None

    def clean_study_level(self, value: Any) -> Tuple[Optional[str], Optional[str]]:
        """
        Clean study level value.

        Args:
            value: Study level value to clean

        Returns:
            Tuple of (cleaned study level or None, error message or None)
        """
        if value is None or (isinstance(value, str) and not value.strip()):
            return None, None

        level_str = str(value).lower().strip()

        # Check in study level map
        if level_str in STUDY_LEVEL_MAP:
            return STUDY_LEVEL_MAP[level_str], None

        # Return as-is if not in map (keep original formatting)
        return str(value).strip(), None

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
        if value is None:
            # hasVisa defaults to False, others to None
            default_value = False if 'visa' in field_name.lower() else None
            return default_value, None, None

        # If already a boolean
        if isinstance(value, bool):
            return value, None, None

        # Convert to string and normalize
        str_value = str(value).strip()

        if not str_value:
            # Empty: hasVisa defaults to False, others to None
            default_value = False if 'visa' in field_name.lower() else None
            return default_value, None, None

        # Handle NaN
        if str_value.lower() == 'nan':
            # NaN: hasVisa defaults to False, others to None
            default_value = False if 'visa' in field_name.lower() else None
            return default_value, None, None

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
            source_col_normalized = normalize_column_name(source_col)

            if api_field is None:
                continue  # Skip unmapped columns

            # Special handling for isFirstYearStudy field - prefer is_first_year_study over first_year
            if api_field == 'isFirstYearStudy':
                # Skip 'first_year' (year value) if 'is_first_year_study' (boolean) column exists
                if source_col_normalized == normalize_column_name('first_year') and has_is_first_year_study:
                    continue  # Skip the year column, use is_first_year_study instead
                # Only process if it's is_first_year_study OR first_year when is_first_year_study doesn't exist
                cleaned, error = self.clean_boolean(value)
                if error:
                    field_errors[api_field] = error
                if cleaned is not None:
                    transformed[api_field] = cleaned
                continue

            # Apply appropriate cleaning based on field type
            if api_field == 'birthDate':
                cleaned, error = self.clean_date(value)
                if error:
                    field_errors[api_field] = error
                if cleaned:
                    transformed[api_field] = cleaned

            elif api_field in ['phoneNumberFr', 'phoneNumberCg']:
                cleaned, error = self.clean_phone(value)
                if error:
                    field_errors[api_field] = error
                if cleaned:
                    transformed[api_field] = cleaned

            elif api_field in ['hasPassportCg', 'hasVisa', 'hasSchoolCertificate']:
                # These fields may contain URLs to documents
                cleaned, error, document_url = self.clean_document_field(value, api_field)
                if error:
                    field_errors[api_field] = error
                if cleaned is not None:
                    transformed[api_field] = cleaned
                # If there's a document URL, create a document entry
                if document_url:
                    # Determine document type from field name
                    doc_type = api_field.replace('has', '')  # PassportCg, Visa, SchoolCertificate
                    documents.append({
                        'type': doc_type,
                        'url': document_url,
                        'field': api_field
                    })

            elif api_field == 'otherAssociations':
                # Regular boolean field
                cleaned, error = self.clean_boolean(value)
                if error:
                    field_errors[api_field] = error
                if cleaned is not None:
                    transformed[api_field] = cleaned

            elif api_field == 'gender':
                cleaned, error = self.clean_gender(value)
                if error:
                    field_errors[api_field] = error
                if cleaned:
                    transformed[api_field] = cleaned

            elif api_field == 'email':
                cleaned, error = self.clean_email(value)
                if error:
                    field_errors[api_field] = error
                if cleaned:
                    transformed[api_field] = cleaned

            elif api_field == 'status':
                cleaned, error = self.clean_status(value)
                if error:
                    field_errors[api_field] = error
                if cleaned:
                    transformed[api_field] = cleaned

            elif api_field == 'membershipType':
                cleaned, error = self.clean_membership_type(value)
                if error:
                    field_errors[api_field] = error
                if cleaned:
                    transformed[api_field] = cleaned

            elif api_field == 'trainingCycle':
                cleaned, error = self.clean_training_cycle(value)
                if error:
                    field_errors[api_field] = error
                if cleaned:
                    transformed[api_field] = cleaned

            elif api_field == 'studyLevel':
                cleaned, error = self.clean_study_level(value)
                if error:
                    field_errors[api_field] = error
                if cleaned:
                    transformed[api_field] = cleaned

            elif api_field == 'contribution':
                # Special handling: Check if it's 'nan' first
                if value is None:
                    continue
                
                # Handle pandas/numpy NaN
                try:
                    import pandas as pd
                    import numpy as np
                    if pd.isna(value) or (isinstance(value, float) and np.isnan(value)):
                        continue
                except (ImportError, TypeError):
                    pass
                
                # Check for NaN string representation
                if isinstance(value, str) and value.strip().lower() in ('nan', 'nat', 'none', ''):
                    continue

                # Try to parse as number
                try:
                    str_value = str(value).strip()
                    # Check again after conversion to string
                    if str_value.lower() in ('nan', 'nat', 'none', ''):
                        continue
                    # Remove currency symbols
                    clean_num = str_value.replace('€', '').replace('$', '').replace(',', '.').strip()
                    amount = float(clean_num)
                    # Final check: ensure the float is not NaN
                    if amount != amount:  # NaN != NaN is True
                        continue
                    transformed['contribution'] = amount
                except (ValueError, AttributeError):
                    # Not a number - treat as status string
                    status_str = str(value).lower().strip()
                    if status_str in CONTRIBUTION_STATUS_MAP:
                        transformed['contributionStatus'] = CONTRIBUTION_STATUS_MAP[status_str]
                    else:
                        # Invalid status - default to pending
                        transformed['contributionStatus'] = 'pending'

            elif api_field == 'contributionStatus':
                # Direct contribution status field
                if value is None:
                    continue
                
                # Handle pandas/numpy NaN
                try:
                    import pandas as pd
                    import numpy as np
                    if pd.isna(value) or (isinstance(value, float) and np.isnan(value)):
                        continue
                except (ImportError, TypeError):
                    pass
                
                # Check for NaN string representation
                status_str = str(value).lower().strip()
                if status_str in ('nan', 'nat', 'none', ''):
                    continue

                if status_str in CONTRIBUTION_STATUS_MAP:
                    transformed[api_field] = CONTRIBUTION_STATUS_MAP[status_str]
                elif status_str in CONTRIBUTION_STATUS_VALUES:
                    transformed[api_field] = status_str
                else:
                    field_errors[api_field] = f"Unknown contribution status: {value}"

            else:
                # Text fields - but skip 'nan' values
                if value is None:
                    continue
                
                # Handle pandas/numpy NaN
                try:
                    import pandas as pd
                    import numpy as np
                    if pd.isna(value) or (isinstance(value, float) and np.isnan(value)):
                        continue
                except (ImportError, TypeError):
                    pass
                
                # Check for NaN string representation
                str_value = str(value).strip()
                if str_value.lower() in ('nan', 'nat', 'none', ''):
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
        if 'status' not in data or not data['status']:
            data['status'] = DEFAULT_STATUS

        if 'membershipType' not in data or not data['membershipType']:
            data['membershipType'] = DEFAULT_MEMBERSHIP_TYPE

        if 'contributionStatus' not in data or not data['contributionStatus']:
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
        required_fields = ['firstName', 'lastName', 'email', 'status', 'membershipType']
        for field in required_fields:
            if field not in data or not data[field]:
                errors.append(f"Missing required field: {field}")

        # Validate enum values
        if 'gender' in data and data['gender']:
            if data['gender'] not in GENDER_VALUES:
                errors.append(f"Invalid gender value: {data['gender']}")

        if 'status' in data and data['status']:
            if data['status'] not in STATUS_VALUES:
                errors.append(f"Invalid status value: {data['status']}")

        if 'membershipType' in data and data['membershipType']:
            if data['membershipType'] not in MEMBERSHIP_TYPE_VALUES:
                errors.append(f"Invalid membershipType value: {data['membershipType']}")

        return len(errors) == 0, errors


