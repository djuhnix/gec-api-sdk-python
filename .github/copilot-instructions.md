# GEC API SDK - Python Client

This is a Python SDK for the GEC (Gestion des Étudiants Congolais) API, auto-generated from OpenAPI spec using OpenAPI Generator.

## Project Structure

- **`gec_api_sdk/`** - Generated SDK code (API clients, models, configuration)
  - `api/` - API endpoint classes (DocumentApi, MemberApi, UserApi, etc.)
  - `models/` - Pydantic models for API resources
  - `api_client.py` - Core API client with request handling
  - `configuration.py` - SDK configuration (host, auth, etc.)
  
- **`scripts/`** - Custom utilities for bulk operations
  - `import_members.py` - CLI tool for importing members from Excel/Google Sheets
  - `helpers/` - Import script modules (data processing, validation, sheet reading)
  
- **`test/`** - Auto-generated pytest tests for SDK models and APIs
- **`docs/`** - Auto-generated API documentation

## Build, Test, and Lint

### Installation
```bash
# Install SDK dependencies
pip install -r requirements.txt

# Install dev/test dependencies
pip install -r test-requirements.txt
```

### Running Tests
```bash
# Run all tests with coverage
pytest --cov=gec_api_sdk

# Run specific test file
pytest test/test_member_api.py

# Run with tox (tests across Python 3.9-3.13)
tox
```

### Linting
```bash
# Flake8 (available via dev dependencies)
flake8 gec_api_sdk/

# Type checking with mypy
mypy gec_api_sdk/
```

## Key Architecture Concepts

### Generated vs Custom Code

**Generated code** (DO NOT manually edit):
- All files in `gec_api_sdk/` except customizations you explicitly protect via `.openapi-generator-ignore`
- All files in `test/` (auto-generated tests)
- Generated from OpenAPI spec using: `openapi-generator-cli generate -i spec.yaml -g python`

**Custom code** (safe to edit):
- Everything in `scripts/` directory
- `.env` configuration files
- This instructions file

### SDK Usage Pattern

The SDK uses a context manager pattern with Bearer JWT authentication:

```python
import gec_api_sdk
from gec_api_sdk.rest import ApiException

configuration = gec_api_sdk.Configuration(
    host="http://localhost",
    access_token=os.environ["BEARER_TOKEN"]
)

with gec_api_sdk.ApiClient(configuration) as api_client:
    api_instance = gec_api_sdk.MemberApi(api_client)
    response = api_instance.api_members_get_collection(page=1)
```

### Member Import Scripts Architecture

The `scripts/` directory implements a modular bulk import system:

1. **`import_members.py`** - CLI entry point with argparse
2. **`helpers/member_importer.py`** - Orchestrates the import workflow
3. **`helpers/sheet_reader.py`** - Abstracts Excel vs Google Sheets reading
4. **`helpers/data_processor.py`** - Validates and transforms data
5. **`helpers/duplicate_checker.py`** - Checks for existing members by email
6. **`helpers/config.py`** - Column mappings and constants
7. **`helpers/utils.py`** - Logging, formatting, file utilities

**Data flow**: CSV/Excel/GSheet → SheetReader → DataProcessor (validate/clean) → DuplicateChecker → MemberImporter → SDK API calls

## Codebase Conventions

### Import Script Column Mapping

The import scripts support **dual column name conventions**:
- **Excel/English**: `last_name`, `first_name`, `email`, `birth_date`, etc.
- **Google Sheets/French**: `Nom`, `Prénom`, `Email`, `Date de naissance`, etc.

Mappings defined in `scripts/helpers/config.py`:
- `EXCEL_COLUMN_MAP` - English to API field mapping
- `GSHEET_COLUMN_MAP` - French to API field mapping

Both map to the same API field names in the SDK's `MemberMemberWrite` model.

### Data Validation Patterns

Import scripts perform extensive data cleaning:
- **Enums**: French → English mapping (e.g., "Homme" → "male", "Actif" → "active")
- **Booleans**: Multiple formats accepted ("oui", "yes", "x", "1" → `True`)
- **Dates**: Multiple formats parsed (DD/MM/YYYY, YYYY-MM-DD, etc.) → ISO format
- **Phone numbers**: Auto-prefix French numbers with +33, remove formatting
- **Contribution field**: Accepts both numeric values (amount) and status strings

**Pattern**: Each field type has a dedicated `clean_*` method in `MemberDataProcessor` that returns `(cleaned_value, error_message)`.

### Error Handling in Imports

Failed records are exported to Excel with:
- All original columns preserved
- `error_reason` - Human-readable error description
- `error_timestamp` - When the error occurred

Users can correct errors in the export and re-import it. The importer logs anonymized data for privacy.

### Stop-on-Error Behavior

The member importer includes a `stop_on_error` mode that halts on first failure for debugging (see `STOP_ON_ERROR.md` for details). Default is continue-on-error with summary at end.

### Environment Configuration

- **`.env`** - Local environment variables (GEC_API_HOST, GEC_API_TOKEN, GOOGLE_CREDENTIALS_PATH)
- **`.env.example`** - Template for required variables
- Scripts use `python-dotenv` to load `.env` automatically

### API Resource Types

The API uses API Platform (Symfony) conventions:
- Resources: Member, User, Event, Task, Donation, Document, EmailTemplate, RSVP
- Collections: GET `/api/members` (paginated with Hydra)
- Items: GET/PUT/DELETE `/api/members/{id}`
- Create: POST `/api/members`

### Pydantic Models

SDK models use Pydantic v2:
- Models have Read/Write variants (e.g., `MemberMemberRead`, `MemberMemberWrite`)
- JSON-LD and CSV serialization variants available
- Use `model.model_dump()` (not `dict()`) for serialization

### Google Sheets Authentication

Import scripts support two auth methods:
- **OAuth2**: For local/interactive use (credentials.json → token.json)
- **Service Account**: For automation (service account JSON key + sheet sharing)

Configured via `--auth-method` flag and `GOOGLE_CREDENTIALS_PATH` env var.

## Running Import Scripts

```bash
cd scripts

# Excel import
python import_members.py --source excel --input ../data/members.xlsx

# Google Sheets with OAuth2
python import_members.py \
  --source gsheet \
  --input "https://docs.google.com/spreadsheets/d/SHEET_ID" \
  --auth-method oauth2

# Dry run (validate without creating)
python import_members.py --source excel --input data.xlsx --dry-run

# Stop on first error
python import_members.py --source excel --input data.xlsx --stop-on-error
```

## CI/CD

GitHub Actions workflow runs on push/PR:
- Runs pytest with coverage across Python 3.9-3.13
- No linting step in CI (but flake8/mypy available locally)

## Regenerating the SDK

When the OpenAPI spec changes:

1. Update `.openapi-generator-ignore` to protect custom files
2. Run generator: `openapi-generator-cli generate -i spec.yaml -g python -o .`
3. Review changes, especially to `gec_api_sdk/` core files
4. Re-run tests to verify compatibility

The SDK version is defined in `setup.py` and `pyproject.toml` (currently 0.1.0).
