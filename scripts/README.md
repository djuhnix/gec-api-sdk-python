# Member Import Scripts

This directory contains scripts for importing member data from Excel and Google Sheets into the GEC API database.

## Features

- ✅ Import from Excel (.xlsx, .xls) files
- ✅ Import from Google Sheets (OAuth2 or Service Account)
- ✅ Duplicate detection by email
- ✅ Data validation and cleaning
- ✅ Failed records export for manual correction
- ✅ Batch processing with progress logging
- ✅ Dry-run mode for validation

## Installation

1. Install required dependencies:
```bash
pip install -r requirements.txt
```

2. Copy the environment template and configure:
```bash
cp .env.example .env
# Edit .env with your API credentials
```

## Configuration

### Environment Variables

Create a `.env` file in the project root with:

```env
GEC_API_HOST=http://localhost
GEC_API_TOKEN=your_jwt_token_here
GOOGLE_CREDENTIALS_PATH=path/to/credentials.json
```

### Google Sheets Authentication

#### OAuth2 (Recommended for local use)
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a project and enable Google Sheets API
3. Create OAuth2 credentials (Desktop application)
4. Download `credentials.json`
5. Set `GOOGLE_CREDENTIALS_PATH` to the file path

#### Service Account (Recommended for automation)
1. Create a service account in Google Cloud Console
2. Download the JSON key file
3. Share your Google Sheet with the service account email
4. Set `GOOGLE_CREDENTIALS_PATH` to the key file path

## Usage

### Basic Excel Import

```bash
cd scripts
python import_members.py --source excel --input ../data/members.xlsx
```

### Google Sheets Import (OAuth2)

```bash
cd scripts
python import_members.py \
    --source gsheet \
    --input "https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID" \
    --auth-method oauth2 \
    --credentials-path ../credentials.json
```

### Google Sheets Import (Service Account)

```bash
cd scripts
python import_members.py \
    --source gsheet \
    --input "YOUR_SHEET_ID" \
    --auth-method service-account \
    --credentials-path ../service-account-key.json \
    --sheet-name "Demande d'adhésion"
```

### Dry Run (Validation Only)

```bash
python import_members.py --source excel --input data.xlsx --dry-run
```

### Custom API Configuration

```bash
python import_members.py \
    --source excel \
    --input data.xlsx \
    --api-host https://api.example.com \
    --api-token YOUR_JWT_TOKEN
```

### All Options

```bash
python import_members.py --help
```

## Column Mappings

### Excel Sheet Columns

The script expects these column names (case-insensitive):

| Excel Column           | API Field             | Required | Type    |
|------------------------|-----------------------|----------|---------|
| last_name              | lastName              | ✅       | String  |
| first_name             | firstName             | ✅       | String  |
| email                  | email                 | ✅       | String  |
| status                 | status                | Auto     | Enum    |
| membership_type        | membershipType        | Auto     | Enum    |
| birth_date             | birthDate             | ❌       | Date    |
| gender                 | gender                | ❌       | Enum    |
| postal_address         | postalAddress         | ❌       | String  |
| city                   | city                  | ❌       | String  |
| postal_code            | postalCode            | ❌       | String  |
| phone_number_fr        | phoneNumberFr         | ❌       | String  |
| training_cycle         | trainingCycle         | ❌       | String  |
| study_level            | studyLevel            | ❌       | String  |
| formation              | formation             | ❌       | String  |
| establishment          | establishment         | ❌       | String  |
| first_year             | firstYear             | ❌       | Boolean |
| other_associations     | otherAssociations     | ❌       | Boolean |
| associations_names     | associationNames      | ❌       | String  |
| has_visa               | hasVisa               | ❌       | Boolean |
| has_school_certificate | hasSchoolCertificate  | ❌       | Boolean |
| photo_url              | photoUrl              | ❌       | String  |
| contribution           | contribution/contributionStatus | ❌ | Number/Status |

**Special Field Handling:**

**Contribution Field**:
The `contribution` field accepts both numeric values and status strings:
- **Numeric value** (e.g., `50`, `75.50`) → Sets `contribution` amount
- **Status string** (e.g., `Attente`, `Payé`) → Sets `contributionStatus`
- Valid status values: `paid`, `payé`, `pending`, `attente`
- Invalid status defaults to `pending`

**Default Values:**
- `status`: Defaults to `expired` if not provided
- `membershipType`: Defaults to `student` if not provided

### Google Sheets Columns (French)

| Google Sheets Column                                        | API Field            |
|-------------------------------------------------------------|----------------------|
| Nom                                                         | lastName             |
| Prénom                                                      | firstName            |
| Email                                                       | email                |
| Date de naissance                                           | birthDate            |
| Sexe                                                        | gender               |
| Téléphone (+33)                                             | phoneNumberFr        |
| Téléphone (+242)                                            | phoneNumberCg        |
| Adresse postale                                             | postalAddress        |
| Code postal                                                 | postalCode           |
| Ville                                                       | city                 |
| Première année                                              | firstYear            |
| Formation                                                   | formation            |
| Etablissement                                               | establishment        |
| Niveau d'étude                                              | studyLevel           |
| Cycle de formation                                          | trainingCycle        |
| Etes-vous déjà engagé dans une ou plusieurs association(s) ? | otherAssociations    |
| Si oui, lesquelles                                          | associationNames     |
| Passeport CG                                                | hasPassportCg        |
| TS ou VLS-TS                                                | hasVisa              |
| Certificat Scolarité                                        | hasSchoolCertificate |
| Photo                                                       | photoUrl             |
| Statut                                                      | status               |
| Cotisation                                                  | contribution         |

## Data Validation

### Enum Values

**Gender:** `male`, `female`, `other`
- French mappings: Homme→male, Femme→female, H→male, F→female

**Status:** `active`, `pending`, `expired`, `suspended`
- French mappings: Actif→active, En attente→pending

**Membership Type:** `student`, `active`, `sponsor`, `alumni`
- French mappings: Étudiant→student, Actif→active

### Boolean Values

Accepted values (case-insensitive):
- **True:** oui, yes, true, 1, x, ok, checked
- **False:** non, no, false, 0, (empty)

### Date Formats

Supported date formats:
- `DD/MM/YYYY` (31/12/2023)
- `YYYY-MM-DD` (2023-12-31)
- `DD-MM-YYYY` (31-12-2023)
- `MM/DD/YYYY` (12/31/2023)
- `YYYY/MM/DD` (2023/12/31)
- `DD.MM.YYYY` (31.12.2023)

### Phone Numbers

- Automatically adds `+33` prefix for French numbers starting with 0
- Cleans spaces, dashes, and dots
- Validates format: `+CCXXXXXXXXXX`

## Output

### Success Summary

```
==================================================
IMPORT SUMMARY
==================================================
Total Records:     100
Success:           85
Failed:            10
Duplicates:        5
Skipped:           0
==================================================
Failed records saved to: failed_imports_20260214_143022.xlsx
==================================================
```

### Failed Records File

Failed records are saved to an Excel file with:
- All original columns
- `error_reason`: Description of why the record failed
- `error_timestamp`: When the error occurred

You can correct the errors and re-import the failed records file.

## Troubleshooting

### Authentication Errors

**Problem:** `401 Unauthorized` or `403 Forbidden`

**Solution:**
- Check your API token is valid
- Ensure token has required permissions
- Verify API host URL is correct

### Google Sheets Errors

**Problem:** `gspread.exceptions.SpreadsheetNotFound`

**Solution:**
- Verify spreadsheet URL/ID is correct
- For service account: Share sheet with service account email
- For OAuth2: Ensure you've authorized the application

### Missing Columns

**Problem:** Required fields missing

**Solution:**
- Column matching is case-insensitive
- Check column names match expected format
- Review column mappings in documentation
- Use `--dry-run` to test without creating records

### Validation Errors

**Problem:** Data validation failures

**Solution:**
- Check enum values match accepted values
- Verify date formats are supported
- Ensure email addresses are valid
- Review failed records file for specific errors

### Import Performance

**Problem:** Slow import for large datasets

**Solution:**
- Adjust batch size: `--batch-size 100`
- Check network latency to API
- Use service account for Google Sheets (faster than OAuth2)

## Module Structure

```
scripts/
.
├── helpers
│ ├── config.py             # Configuration and constants
│ ├── data_processor.py     # Data cleaning and validation
│ ├── duplicate_checker.py  # Duplicate detection
│ ├── member_importer.py    # Main import orchestration
│ ├── sheet_reader.py       # Excel and Google Sheets readers
│ └── utils.py              # Utility functions
├── import_members.py       # CLI entry point
├── sample_data.csv         # Sample Excel data for testing
└── test_setup.py           # Test setup
```

## Development

### Adding New Column Mappings

Edit `scripts/helpers/config.py`:

```python
EXCEL_COLUMN_MAP = {
    'new_column': 'newApiField',
    # ... existing mappings
}
```

### Customizing Data Cleaning

Edit `scripts/helpers/data_processor.py` in the `MemberDataProcessor` class:

```python
def clean_custom_field(self, value):
    # Your cleaning logic
    return cleaned_value, error_message
```

### Testing

Run a dry-run to test without creating records:

```bash
python import_members.py --source excel --input test.xlsx --dry-run --log-level DEBUG
```

## License

Part of the GEC API SDK project.
