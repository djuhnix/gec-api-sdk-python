# Quick Start Guide - Member Import

This guide will help you get started with importing member data.

## Step 1: Install Dependencies

```bash
cd /home/outscale/PhpstormProjects/gec-api-sdk-python
pip install -r requirements.txt
```

## Step 2: Configure Environment

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your values
nano .env
```

Set these values in `.env`:
```env
GEC_API_HOST=http://localhost:8000  # Your API URL
GEC_API_TOKEN=your_jwt_token_here   # Your JWT token
```

## Step 3: Test the Setup

```bash
cd scripts
python test_setup.py
```

This will verify all modules and dependencies are correctly installed.

## Step 4: Try a Dry Run

Test with the sample data (validation only, no database changes):

```bash
python import_members.py --source excel --input sample_data.csv --dry-run
```

## Step 5: Import Real Data

### From Excel:

```bash
python import_members.py --source excel --input /path/to/your/file.xlsx
```

### From Google Sheets (OAuth2):

```bash
# First time - you'll be prompted to authorize in browser
python import_members.py \
    --source gsheet \
    --input "https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID" \
    --auth-method oauth2 \
    --credentials-path /path/to/credentials.json
```

## Common Use Cases

### 1. Validate Data Before Import

```bash
python import_members.py --source excel --input data.xlsx --dry-run
```

### 2. Import with Custom Output Path for Failures

```bash
python import_members.py \
    --source excel \
    --input data.xlsx \
    --output-failed failures_2026.xlsx
```

### 3. Import with Debug Logging

```bash
python import_members.py \
    --source excel \
    --input data.xlsx \
    --log-level DEBUG
```

### 4. Import Specific Google Sheet Tab

```bash
python import_members.py \
    --source gsheet \
    --input "YOUR_SHEET_ID" \
    --sheet-name "Demande d'adhésion" \
    --auth-method oauth2
```

## Understanding the Output

### Successful Import:
```
==================================================
IMPORT SUMMARY
==================================================
Total Records:     100
Success:           95
Failed:            5
Duplicates:        0
Skipped:           0
==================================================
Failed records saved to: failed_imports_20260214_143022.xlsx
==================================================
```

### Failed Records File:

The failed records Excel file contains:
- All original columns from your source
- `error_reason`: Why it failed (e.g., "Invalid email format")
- `error_timestamp`: When the error occurred

You can:
1. Fix the errors in the Excel file
2. Remove the error columns
3. Re-import the corrected file

## Troubleshooting

### "No module named 'pandas'"

Install dependencies:
```bash
pip install -r requirements.txt
```

### "API token is required"

Set your token in `.env` or pass it via command line:
```bash
python import_members.py --source excel --input data.xlsx --api-token YOUR_TOKEN
```

### "Invalid email format"

Check your data has valid email addresses. The script expects standard format:
`name@domain.com`

### "Duplicate email"

The email already exists in the database. The script skips duplicates by default.
(Future: use `--update-duplicates` to update existing records)

### Google Sheets: "SpreadsheetNotFound"

- Verify the spreadsheet URL/ID is correct
- For service account: Share the sheet with the service account email
- For OAuth2: Make sure you authorize when prompted

## Next Steps

- Read the full documentation: `scripts/README.md`
- Check column mappings for your data format
- Set up automated imports with cron jobs
- Customize data cleaning rules in `scripts/config.py`

## Getting Help

Check the logs for detailed error messages:
```bash
python import_members.py --source excel --input data.xlsx --log-level DEBUG
```

The log will show:
- Which columns were found
- Data transformation steps
- Validation errors
- API communication details

