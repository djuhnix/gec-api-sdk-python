"""
Utility functions for member import scripts.
"""
import hashlib
import logging
import os
import re
from datetime import datetime
from typing import Dict, Optional, Any


def setup_logging(level: str = 'INFO') -> None:
    """
    Configure logging for the import scripts.

    Logs are saved to:
    - Console (stdout)
    - File: logs/import_YYYYMMDD_HHMMSS.log

    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    # Create logs directory if it doesn't exist
    log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Generate log filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file = os.path.join(log_dir, f'import_{timestamp}.log')

    # Configure logging with both console and file handlers
    log_level = getattr(logging, level.upper())

    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Get root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)

    # Remove existing handlers to avoid duplicates
    root_logger.handlers = []

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)

    # File handler
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)
    root_logger.addHandler(file_handler)

    # Log the log file location
    root_logger.info(f"Logging to file: {log_file}")


def load_env_variables() -> Dict[str, str]:
    """
    Load and validate required environment variables.

    Returns:
        Dictionary of environment variables

    Raises:
        ValueError: If required variables are missing
    """
    from dotenv import load_dotenv

    # Load .env file if it exists
    load_dotenv()

    api_host = os.getenv('GEC_API_HOST', 'http://localhost')
    api_token = os.getenv('GEC_API_TOKEN', '')

    if not api_token:
        logging.warning("GEC_API_TOKEN not set. API calls will fail without authentication.")

    return {
        'api_host': api_host,
        'api_token': api_token,
        'google_credentials_path': os.getenv('GOOGLE_CREDENTIALS_PATH', ''),
    }


def format_summary_table(summary: Dict) -> str:
    """
    Format import summary as an ASCII table.

    Args:
        summary: Dictionary with import results

    Returns:
        Formatted table string
    """
    lines = [
        "=" * 50,
        "IMPORT SUMMARY",
        "=" * 50,
        f"Total Records:     {summary.get('total', 0)}",
        f"Success:           {summary.get('success', 0)}",
        f"Failed:            {summary.get('failed', 0)}",
        f"Duplicates:        {summary.get('duplicates', 0)}",
        f"Skipped:           {summary.get('skipped', 0)}",
        "=" * 50,
    ]

    if summary.get('failed', 0) > 0:
        lines.append(f"Failed records saved to: {summary.get('failed_file', 'N/A')}")
        lines.append("=" * 50)

    return "\n".join(lines)


def get_timestamp() -> str:
    """
    Get current timestamp formatted for filenames.

    Returns:
        Timestamp string (YYYYMMDD_HHMMSS)
    """
    return datetime.now().strftime('%Y%m%d_%H%M%S')


def get_iso_timestamp() -> str:
    """
    Get current timestamp in ISO format.

    Returns:
        ISO format timestamp string
    """
    return datetime.now().isoformat()


def validate_file_path(file_path: str) -> bool:
    """
    Check if a file exists and is readable.

    Args:
        file_path: Path to file

    Returns:
        True if file exists and is readable
    """
    if not os.path.exists(file_path):
        return False
    if not os.path.isfile(file_path):
        return False
    if not os.access(file_path, os.R_OK):
        return False
    return True


def truncate_string(text: Optional[str], max_length: int = 50) -> str:
    """
    Truncate string to maximum length with ellipsis.

    Args:
        text: String to truncate
        max_length: Maximum length

    Returns:
        Truncated string
    """
    if not text:
        return ""
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."


def anonymize_email(email: str) -> str:
    """
    Anonymize an email address while keeping it valid.

    Args:
        email: Original email address

    Returns:
        Anonymized email address
    """
    if not email or '@' not in email:
        return email

    # Create a hash of the email
    email_hash = hashlib.md5(email.lower().encode()).hexdigest()[:8]

    # Get domain, ensure it's valid
    parts = email.split('@')
    domain = parts[1] if len(parts) > 1 and parts[1] else 'example.com'
    
    # Ensure domain has proper format (must have at least one dot for most validators)
    if '.' not in domain:
        domain = f"{domain}.com"

    return f"user_{email_hash}@{domain}"


def anonymize_name(name: str, prefix: str = "User") -> str:
    """
    Anonymize a name by creating a hash-based pseudonym.

    Args:
        name: Original name
        prefix: Prefix for anonymized name (e.g., "User", "Member")

    Returns:
        Anonymized name
    """
    if not name:
        return name

    # Create a short hash
    name_hash = hashlib.md5(name.lower().encode()).hexdigest()[:6]
    return f"{prefix}_{name_hash}"


def anonymize_phone(phone: str) -> str:
    """
    Anonymize a phone number while keeping format.

    Args:
        phone: Original phone number

    Returns:
        Anonymized phone number
    """
    if not phone:
        return phone

    # Keep country code and format, anonymize the rest
    if phone.startswith('+33'):
        return '+33600000000'
    elif phone.startswith('+242'):
        return '+242000000000'
    else:
        # Generic anonymization
        return re.sub(r'\d', '0', phone)


def anonymize_address(address: str) -> str:
    """
    Anonymize an address.

    Args:
        address: Original address

    Returns:
        Anonymized address
    """
    if not address:
        return address

    # Create a generic address based on hash
    addr_hash = hashlib.md5(address.lower().encode()).hexdigest()[:4]
    return f"{addr_hash.upper()} Anonymous Street"


def anonymize_generic_text(text: str, prefix: str = "Text") -> str:
    """
    Anonymize generic text fields (establishment, formation, etc.).

    Args:
        text: Original text
        prefix: Prefix for anonymized text

    Returns:
        Anonymized text
    """
    if not text:
        return text

    # Create a hash-based pseudonym
    text_hash = hashlib.md5(text.lower().encode()).hexdigest()[:6]
    return f"{prefix}_{text_hash}"


def anonymize_postal_code(postal_code: str) -> str:
    """
    Anonymize a postal code while keeping it realistic (max 10 chars).

    Args:
        postal_code: Original postal code

    Returns:
        Anonymized postal code (max 10 characters)
    """
    if not postal_code:
        return postal_code

    # Create a hash and take first 5 digits to create a fake postal code
    code_hash = hashlib.md5(postal_code.lower().encode()).hexdigest()
    # Use first 10 hex chars and convert to look like a postal code
    # Format: XXXXX (5 chars) or XX-XXX (6 chars with dash)
    fake_code = ''.join(filter(str.isalnum, code_hash[:5])).upper()
    
    # Pad with zeros if needed to ensure consistent length
    fake_code = fake_code.ljust(5, '0')[:5]
    
    return fake_code


def anonymize_record(record: Dict[str, Any], fields_to_anonymize: list = None) -> Dict[str, Any]:
    """
    Anonymize sensitive fields in a record.

    Args:
        record: Original record dictionary
        fields_to_anonymize: List of field names to anonymize. If None, uses default list.

    Returns:
        Anonymized record
    """
    if fields_to_anonymize is None:
        # Default fields to anonymize
        fields_to_anonymize = [
            'email', 'first_name', 'last_name', 'firstName', 'lastName',
            'phone_number_fr', 'phone_number_cg', 'phoneNumberFr', 'phoneNumberCg',
            'postal_address', 'postalAddress', 'Téléphone (+33)', 'Téléphone (+242)',
            'Nom', 'Prénom', 'Email', 'Adresse postale',
            'establishment', 'Etablissement', 'formation', 'Formation',
            'city', 'Ville', 'postal_code', 'postalCode', 'Code postal'
        ]

    anonymized = record.copy()

    for field in fields_to_anonymize:
        if field not in anonymized or not anonymized[field]:
            continue

        value = str(anonymized[field])

        # Anonymize based on field type
        if 'email' in field.lower():
            anonymized[field] = anonymize_email(value)
        elif any(name in field.lower() for name in ['first_name', 'firstname', 'prénom', 'prenom']):
            anonymized[field] = anonymize_name(value, "FirstName")
        elif any(name in field.lower() for name in ['last_name', 'lastname', 'nom']):
            anonymized[field] = anonymize_name(value, "LastName")
        elif any(phone in field.lower() for phone in ['phone', 'téléphone', 'telephone']):
            anonymized[field] = anonymize_phone(value)
        elif any(addr in field.lower() for addr in ['address', 'adresse']):
            anonymized[field] = anonymize_address(value)
        elif 'postal_code' in field.lower() or 'postalcode' in field.lower() or 'code postal' in field.lower():
            anonymized[field] = anonymize_postal_code(value)
        elif 'establishment' in field.lower() or 'etablissement' in field.lower():
            anonymized[field] = anonymize_generic_text(value, "Establishment")
        elif 'formation' in field.lower():
            anonymized[field] = anonymize_generic_text(value, "Formation")
        elif 'city' in field.lower() or 'ville' in field.lower():
            anonymized[field] = anonymize_generic_text(value, "City")

    return anonymized


