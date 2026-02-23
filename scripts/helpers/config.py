"""
Configuration module for member import scripts.
Contains column mappings, data cleaning maps, and constants.
"""

import os
from typing import Dict

# Environment variables
GEC_API_HOST = os.getenv('GEC_API_HOST', 'http://localhost:8080')
GEC_API_TOKEN = os.getenv('GEC_API_TOKEN', '')
GOOGLE_CREDENTIALS_PATH = os.getenv('GOOGLE_CREDENTIALS_PATH', '')

# Default values for member creation
DEFAULT_STATUS = 'expired'
DEFAULT_MEMBERSHIP_TYPE = 'student'
DEFAULT_CONTRIBUTION_STATUS = 'pending'  # Default for missing contribution status

# Enum validation sets (from MemberWrite model)
STATUS_VALUES = {'active', 'pending', 'expired', 'suspended'}
MEMBERSHIP_TYPE_VALUES = {'student', 'active', 'sponsor', 'alumni'}
GENDER_VALUES = {'male', 'female', 'other'}
CONTRIBUTION_STATUS_VALUES = {'paid', 'pending'}

# Date formats to try when parsing dates
DATE_FORMATS = [
    '%d/%m/%Y',      # 31/12/2023
    '%Y-%m-%d',      # 2023-12-31
    '%d-%m-%Y',      # 31-12-2023
    '%m/%d/%Y',      # 12/31/2023
    '%Y/%m/%d',      # 2023/12/31
    '%d.%m.%Y',      # 31.12.2023
    '%Y%m%d',        # 20231231
]

# Excel sheet column mappings (Excel column -> API field)
EXCEL_COLUMN_MAP = {
    'last_name': 'lastName',
    'first_name': 'firstName',
    'birth_date': 'birthDate',
    'gender': 'gender',
    'postal_address': 'postalAddress',
    'city': 'city',
    'postal_code': 'postalCode',
    'phone_number_fr': 'phoneNumberFr',
    'membership_type': 'membershipType',
    'training_cycle': 'trainingCycle',
    'study_level': 'studyLevel',
    'formation': 'formation',
    'establishment': 'establishment',
    'email': 'email',
    'first_year': 'isFirstYearStudy',  # Year value that will be converted to boolean (year == current_year)
    'is_first_year_study': 'isFirstYearStudy',  # Alternative: direct boolean value
    'other_associations': 'otherAssociations',
    'associations_names': 'associationNames',
    'association_link': 'associationNames',  # Alternative column name
    'has_visa': 'hasVisa',
    'has_school_certificate': 'hasSchoolCertificate',
    'photo_url': 'photoUrl',
    'status': 'status',
    'contribution': 'contribution',
}

# Google Sheets column mappings (French column names -> API field)
GSHEET_COLUMN_MAP = {
    'nom': 'lastName',
    'prénom': 'firstName',
    'date de naissance': 'birthDate',
    'sexe': 'gender',
    'téléphone (+33)': 'phoneNumberFr',
    'téléphone (+242)': 'phoneNumberCg',
    'email': 'email',
    'adresse postale': 'postalAddress',
    'code postal': 'postalCode',
    'ville': 'city',
    'première année': 'firstYear',
    'formation': 'formation',
    'etablissement': 'establishment',
    'niveau d\'étude': 'studyLevel',
    'niveau d etude': 'studyLevel',  # Alternative without apostrophe
    'cycle de formation': 'trainingCycle',
    'etes-vous déjà engagé dans une ou plusieurs association(s) ?': 'otherAssociations',
    'etes-vous deja engage dans une ou plusieurs association(s) ?': 'otherAssociations',
    'si oui, lesquelles': 'associationNames',
    'passeport cg': 'hasPassportCg',
    'ts ou vls-ts': 'hasVisa',
    'certificat scolarité': 'hasSchoolCertificate',
    'certificat scolarite': 'hasSchoolCertificate',
    'photo': 'photoUrl',
    'statut': 'status',
    'cotisation': 'contribution',
}

# Gender value mappings (various input -> API enum)
GENDER_MAP = {
    # French
    'homme': 'male',
    'femme': 'female',
    'h': 'male',
    'f': 'female',
    'm': 'male',
    # English
    'male': 'male',
    'female': 'female',
    'man': 'male',
    'woman': 'female',
    'other': 'other',
    'autre': 'other',
}

# Boolean value mappings (various input -> bool)
BOOLEAN_MAP = {
    # French
    'oui': True,
    'non': False,
    # English
    'yes': True,
    'no': False,
    'true': True,
    'false': False,
    # Numeric
    '1': True,
    '0': False,
    # Empty/None
    '': False,
    'none': False,
}

# Sample status mappings (for future use with actual data)
STATUS_MAP = {
    'actif': 'active',
    'active': 'active',
    'en attente': 'pending',
    'pending': 'pending',
    'expiré': 'expired',
    'expired': 'expired',
    'suspendu': 'suspended',
    'suspended': 'suspended',
}

# Sample membership type mappings (for future use with actual data)
MEMBERSHIP_TYPE_MAP = {
    'étudiant': 'student',
    'student': 'student',
    'actif': 'active',
    'active': 'active',
    'sponsor': 'sponsor',
    'parrain': 'sponsor',
    'alumni': 'alumni',
    'ancien': 'alumni',
}

# Contribution status mappings
# API expects: 'paid', 'pending'
CONTRIBUTION_STATUS_MAP = {
    'paid': 'paid',
    'payé': 'paid',
    'paye': 'paid',
    'payée': 'paid',
    'payee': 'paid',
    'réglé': 'paid',
    'regle': 'paid',
    'pending': 'pending',
    'attente': 'pending',
    'en attente': 'pending',
    'à payer': 'pending',
    'a payer': 'pending',
    'impayé': 'pending',
    'impaye': 'pending',
}

# Training cycle mappings (actual values from data)
# API expects: 'initial', 'apprenticeship', 'continuing_education'
TRAINING_CYCLE_MAP = {
    'alumuni': 'initial',  # Typo in source data, map to initial
    'alumni': 'initial',
    'apprenticeship': 'apprenticeship',
    'apprentissage': 'apprenticeship',
    'initial': 'initial',
    'initiale': 'initial',
    'continuing_education': 'continuing_education',
    'formation continue': 'continuing_education',
    'cycle 1': 'initial',
    'cycle 2': 'initial',
    'cycle 3': 'initial',
}

# Study level mappings (actual values from data)
STUDY_LEVEL_MAP = {
    'bac+3': 'BAC+3',
    'bac+5': 'BAC+5',
    'licence': 'Licence',
    'master': 'Master',
    'doctorat': 'Doctorat',
    'bts': 'BTS',
    'dut': 'DUT',
}


def normalize_column_name(column_name: str) -> str:
    """
    Normalize column name for case-insensitive matching.
    Converts to lowercase, strips whitespace, and normalizes separators.

    Args:
        column_name: Original column name

    Returns:
        Normalized column name
    """
    if not isinstance(column_name, str):
        return str(column_name).lower().strip()

    normalized = column_name.lower().strip()
    # Remove extra whitespace
    normalized = ' '.join(normalized.split())
    return normalized


def get_column_map(source_type: str) -> Dict[str, str]:
    """
    Get the appropriate column mapping for the source type.

    Args:
        source_type: 'excel' or 'gsheet'

    Returns:
        Dictionary mapping source columns to API fields
    """
    if source_type == 'excel':
        return EXCEL_COLUMN_MAP
    elif source_type == 'gsheet':
        return GSHEET_COLUMN_MAP
    else:
        raise ValueError(f"Unknown source type: {source_type}")

