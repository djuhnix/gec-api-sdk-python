# Member Import Scripts

Scripts to import member data from an Excel file or a Google Sheet directly into the GEC API database.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Environment Setup](#environment-setup)
4. [Running the Script](#running-the-script)
5. [All Command Options](#all-command-options)
6. [Google Sheets Setup](#google-sheets-setup)
7. [Column Reference](#column-reference)
8. [Data Validation Rules](#data-validation-rules)
9. [Understanding the Output](#understanding-the-output)
10. [Troubleshooting](#troubleshooting)

---

## Prerequisites

Before starting, make sure you have the following installed on your computer:

- **Python 3.9 or later** — [Download here](https://www.python.org/downloads/)
  - To check: open a terminal and run `python3 --version`
- **Git** (optional, to clone the project) — [Download here](https://git-scm.com/)

You also need:
- The URL of the GEC API server
- A valid **JWT token** to authenticate with the API (ask your team admin)

---

## Installation

Open a terminal, navigate to the project root, and run these commands **in order**:

```bash
# 1. Go to the project root (adjust the path to where you cloned the project)
cd /path/to/gec-api-sdk-python

# 2. Create a Python virtual environment
#    This is an isolated space for the project's dependencies — it won't affect
#    anything else on your computer.
python3 -m venv .venv

# 3. Activate the virtual environment
#    You must do this every time you open a new terminal before running the scripts.
source .venv/bin/activate          # macOS / Linux
# .venv\Scripts\activate           # Windows (use this line instead)

# 4. Install the required packages
pip install -r requirements.txt
pip install -e .                   # installs the SDK itself
```

> **Note:** When the virtual environment is active, your terminal prompt will show `(.venv)` at the start. If you don't see it, run the `source` command above again.

---

## Environment Setup

The script reads your API credentials from a `.env` file so you don't have to type them every time.

**Step 1 — Create the file:**

```bash
# From the project root
cp .env.example .env
```

**Step 2 — Edit `.env` with a text editor:**

```bash
nano .env          # macOS / Linux terminal editor (Ctrl+O to save, Ctrl+X to exit)
# or open the file in any editor (VS Code, Notepad++, etc.)
```

**Step 3 — Fill in your values:**

```env
# The URL of the GEC API server — no trailing slash
# Examples:
#   Local development:  http://localhost:8080
#   Production server:  https://api.gec-asso.fr
GEC_API_HOST=http://localhost:8080

# Your JWT bearer token — ask your team admin if you don't have one
# It looks like a long string of random characters: eyJhbGciOiJSUz...
GEC_API_TOKEN=your_jwt_token_here

# Only needed for Google Sheets imports — leave blank otherwise
GOOGLE_CREDENTIALS_PATH=
```

> **Security:** Never share your `.env` file or commit it to Git. It is already listed in `.gitignore`.

---

## Running the Script

All commands below assume:
- Your terminal is open in the **`scripts/`** directory
- The virtual environment is **active** (you see `(.venv)` in your prompt)

```bash
cd scripts
```

### Import from an Excel file

```bash
python3 import_members.py --source excel --input ../data/members.xlsx
```

Replace `../data/members.xlsx` with the actual path to your file.

### Dry run — validate without creating anything

Always do this first when importing a new file. It checks your data for errors without touching the database.

```bash
python3 import_members.py --source excel --input ../data/members.xlsx --dry-run
```

### Import from Google Sheets

See [Google Sheets Setup](#google-sheets-setup) first, then:

```bash
# OAuth2 (for local/interactive use — opens a browser to authorize)
python3 import_members.py \
    --source gsheet \
    --input "https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID" \
    --auth-method oauth2 \
    --credentials-path ../credentials.json

# Service account (for automation — no browser needed)
python3 import_members.py \
    --source gsheet \
    --input "YOUR_SHEET_ID" \
    --auth-method service-account \
    --credentials-path ../service-account-key.json \
    --sheet-name "Demande d'adhésion"
```

### Re-import a failed records file

After an import, records that failed are saved to an Excel file. Fix the errors in that file, then re-import it:

```bash
python3 import_members.py --source excel --input failed_imports_20260214_143022.xlsx
```

---

## All Command Options

```
usage: import_members.py [-h] --source {excel,gsheet} --input INPUT
                         [--sheet-name SHEET_NAME]
                         [--output-failed OUTPUT_FAILED]
                         [--output-format {excel,csv}]
                         [--api-host API_HOST] [--api-token API_TOKEN]
                         [--auth-method {oauth2,service-account}]
                         [--credentials-path CREDENTIALS_PATH]
                         [--dry-run] [--anonymize] [--stop-on-error]
                         [--batch-size BATCH_SIZE] [--concurrency CONCURRENCY]
                         [--log-level {DEBUG,INFO,WARNING,ERROR}]
```

| Option               | Description                                                                | Default                         |
|----------------------|----------------------------------------------------------------------------|---------------------------------|
| `--source`           | Where to read data from: `excel` or `gsheet`                               | *(required)*                    |
| `--input`            | File path (Excel) or spreadsheet URL/ID (Google Sheets)                    | *(required)*                    |
| `--sheet-name`       | Worksheet tab name (Google Sheets only)                                    | `Demande d'adhésion`            |
| `--output-failed`    | Path for the failed records output file                                    | `failed_imports_TIMESTAMP.xlsx` |
| `--output-format`    | Format for failed records file: `excel` or `csv`                           | `excel`                         |
| `--api-host`         | API server URL (overrides `GEC_API_HOST` from `.env`)                      | from `.env`                     |
| `--api-token`        | JWT token (overrides `GEC_API_TOKEN` from `.env`)                          | from `.env`                     |
| `--auth-method`      | Google Sheets auth: `oauth2` or `service-account`                          | `oauth2`                        |
| `--credentials-path` | Path to Google credentials file (overrides `.env`)                         | from `.env`                     |
| `--dry-run`          | Validate data and show what would happen, without creating anything        | off                             |
| `--anonymize`        | Mask names, emails, phones in logs (useful when sharing logs with support) | off                             |
| `--stop-on-error`    | Stop immediately after the first validation or API error                   | off                             |
| `--batch-size`       | How many records to prepare before sending them to the API                 | `50`                            |
| `--concurrency`      | How many API calls to fire in parallel per batch                           | `10`                            |
| `--log-level`        | How much detail to show: `DEBUG`, `INFO`, `WARNING`, `ERROR`               | `INFO`                          |

---

## Google Sheets Setup

### Option A — OAuth2 (recommended for manual/local use)

This method opens a browser window the first time to authorize access to your Google account.

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a project (or select an existing one)
3. Enable the **Google Sheets API**: *APIs & Services → Library → Google Sheets API → Enable*
4. Create credentials: *APIs & Services → Credentials → Create Credentials → OAuth client ID*
   - Application type: **Desktop app**
5. Download the `credentials.json` file
6. Set `GOOGLE_CREDENTIALS_PATH=/path/to/credentials.json` in your `.env`

The first time you run the script, a browser window will open to authorize. A `token.json` file will be saved next to `credentials.json` so future runs won't need the browser.

### Option B — Service Account (recommended for automation / cron jobs)

This method uses a "robot" Google account that can access the sheet without a browser.

1. In [Google Cloud Console](https://console.cloud.google.com/), go to *APIs & Services → Credentials → Create Credentials → Service account*
2. Give it a name, then click *Done*
3. Click the service account email → *Keys* tab → *Add Key → Create new key → JSON* → Download the file
4. **Share your Google Sheet** with the service account's email address (found in the downloaded JSON under `client_email`) — give it *Viewer* access
5. Set `GOOGLE_CREDENTIALS_PATH=/path/to/service-account-key.json` in your `.env`

---

## Column Reference

### Excel file columns

The script matches columns by name (case-insensitive, spaces and underscores are equivalent).

| Column name              | API field                             | Required | Format                          |
|--------------------------|---------------------------------------|----------|---------------------------------|
| `last_name`              | `lastName`                            | ✅        | Text                            |
| `first_name`             | `firstName`                           | ✅        | Text                            |
| `email`                  | `email`                               | ✅        | `name@domain.com`               |
| `status`                 | `status`                              | auto     | See [Enums](#enum-values)       |
| `membership_type`        | `membershipType`                      | auto     | See [Enums](#enum-values)       |
| `birth_date`             | `birthDate`                           | ❌        | See [Dates](#date-formats)      |
| `gender`                 | `gender`                              | ❌        | See [Enums](#enum-values)       |
| `postal_address`         | `postalAddress`                       | ❌        | Text                            |
| `city`                   | `city`                                | ❌        | Text                            |
| `postal_code`            | `postalCode`                          | ❌        | Text                            |
| `phone_number_fr`        | `phoneNumberFr`                       | ❌        | Phone number                    |
| `training_cycle`         | `trainingCycle`                       | ❌        | Text                            |
| `study_level`            | `studyLevel`                          | ❌        | Text                            |
| `formation`              | `formation`                           | ❌        | Text                            |
| `establishment`          | `establishment`                       | ❌        | Text                            |
| `first_year`             | `firstYear`                           | ❌        | See [Booleans](#boolean-values) |
| `other_associations`     | `otherAssociations`                   | ❌        | See [Booleans](#boolean-values) |
| `associations_names`     | `associationNames`                    | ❌        | Text                            |
| `has_visa`               | `hasVisa`                             | ❌        | See [Booleans](#boolean-values) |
| `has_school_certificate` | `hasSchoolCertificate`                | ❌        | See [Booleans](#boolean-values) |
| `photo_url`              | `photoUrl`                            | ❌        | URL                             |
| `contribution`           | `contribution` / `contributionStatus` | ❌        | Number or status string         |

**Contribution field:** accepts either a numeric amount (e.g. `50`, `75.50`) or a status string (`paid`, `payé`, `pending`, `attente`). A number sets the contribution amount; a string sets the contribution status.

**Auto-defaulted fields:** `status` defaults to `expired` and `membershipType` to `student` when left blank.

### Google Sheets columns (French)

| Column header                                                | API field              |
|--------------------------------------------------------------|------------------------|
| Nom                                                          | `lastName`             |
| Prénom                                                       | `firstName`            |
| Email                                                        | `email`                |
| Date de naissance                                            | `birthDate`            |
| Sexe                                                         | `gender`               |
| Téléphone (+33)                                              | `phoneNumberFr`        |
| Téléphone (+242)                                             | `phoneNumberCg`        |
| Adresse postale                                              | `postalAddress`        |
| Code postal                                                  | `postalCode`           |
| Ville                                                        | `city`                 |
| Première année                                               | `firstYear`            |
| Formation                                                    | `formation`            |
| Etablissement                                                | `establishment`        |
| Niveau d'étude                                               | `studyLevel`           |
| Cycle de formation                                           | `trainingCycle`        |
| Etes-vous déjà engagé dans une ou plusieurs association(s) ? | `otherAssociations`    |
| Si oui, lesquelles                                           | `associationNames`     |
| Passeport CG                                                 | `hasPassportCg`        |
| TS ou VLS-TS                                                 | `hasVisa`              |
| Certificat Scolarité                                         | `hasSchoolCertificate` |
| Photo                                                        | `photoUrl`             |
| Statut                                                       | `status`               |
| Cotisation                                                   | `contribution`         |

---

## Data Validation Rules

### Enum values

These fields only accept specific values. The script automatically translates French variants.

**`gender`:** `male` · `female` · `other`
> French: `Homme` / `H` → `male` · `Femme` / `F` → `female`

**`status`:** `active` · `pending` · `expired` · `suspended`
> French: `Actif` → `active` · `En attente` / `Pending` → `pending`

**`membershipType`:** `student` · `active` · `sponsor` · `alumni`
> French: `Étudiant` → `student` · `Actif` → `active`

**`trainingCycle`:** `bachelor` · `master` · `doctorate` · `other`

### Boolean values

These fields accept any of the following (case-insensitive):

| Means **true**                                  | Means **false**                          |
|-------------------------------------------------|------------------------------------------|
| `oui`, `yes`, `true`, `1`, `x`, `ok`, `checked` | `non`, `no`, `false`, `0`, or empty cell |

### Date formats

All of the following are accepted for date fields:

| Format       | Example      |
|--------------|--------------|
| `DD/MM/YYYY` | `31/12/2023` |
| `YYYY-MM-DD` | `2023-12-31` |
| `DD-MM-YYYY` | `31-12-2023` |
| `MM/DD/YYYY` | `12/31/2023` |
| `YYYY/MM/DD` | `2023/12/31` |
| `DD.MM.YYYY` | `31.12.2023` |

### Phone numbers

- French numbers starting with `0` are automatically prefixed with `+33` (e.g. `0612345678` → `+33612345678`)
- Spaces, dashes, and dots are stripped automatically
- Expected final format: `+CCXXXXXXXXXX`

---

## Understanding the Output

### Progress logs

While the script runs, it prints one line per record:

```
INFO  Row 1: Successfully created member - jean.dupont@example.com
INFO  Row 2: Skipping duplicate - marie.martin@example.com
WARNING Row 3: Validation failed - Field email: invalid format
```

### Summary at the end

```
==================================================
IMPORT SUMMARY
==================================================
Total Records:     100
Success:            85
Failed:             10
Duplicates:          5
Skipped:             0
==================================================
Failed records saved to: failed_imports_20260214_143022.xlsx
==================================================
```

### Failed records file

When records fail, they are saved to an Excel file containing:
- All the original columns from your source
- `error_reason` — a plain-English description of what went wrong
- `error_timestamp` — when the error occurred

**To fix and retry:** open the file, correct the values, delete the `error_reason` and `error_timestamp` columns, and re-run the script with this file as input.

---

## Troubleshooting

### `ModuleNotFoundError: No module named '...'`

The virtual environment is not active or dependencies are not installed.

```bash
source .venv/bin/activate    # activate the venv
pip install -r requirements.txt
pip install -e .
```

### `401 Unauthorized` or `403 Forbidden`

Your API token is invalid or expired. Ask your admin for a new token and update `GEC_API_TOKEN` in `.env`.

### `Connection refused` / `Could not connect to API`

The API server is not reachable. Check that:
- `GEC_API_HOST` in `.env` is the correct URL
- The server is running (ask your admin)
- You are on the right network (VPN if needed)

### `API token is required`

The `.env` file is missing or `GEC_API_TOKEN` is empty. Verify the file exists and contains a value:

```bash
cat .env | grep GEC_API_TOKEN
```

### `gspread.exceptions.SpreadsheetNotFound`

- Double-check the spreadsheet URL or ID
- **Service account:** make sure you shared the sheet with the service account email (`client_email` in the JSON key file)
- **OAuth2:** re-run — you may need to re-authorize in the browser

### A column is not being recognized

Column matching is case-insensitive and ignores spaces vs. underscores. If a column is still not found:
- Check for invisible characters or extra spaces in the header row of your file
- Compare with the exact names in the [Column Reference](#column-reference)
- Run with `--log-level DEBUG` to see which columns were detected

### Records fail with unexpected enum errors

Run with `--dry-run --log-level DEBUG` to see exactly how each value is being interpreted before anything is created.

### Import is slow for large files

Increase parallelism (safe up to the API server's limit):

```bash
python3 import_members.py --source excel --input data.xlsx --concurrency 20
```

### Something went wrong mid-import — how do I know where it stopped?

Use `--stop-on-error` to halt at the first failure and get the exact row number. The failed records file will also contain `error_reason` for every row that did not succeed.

---

## Module Structure

```
scripts/
├── import_members.py          # CLI entry point — run this
├── helpers/
│   ├── config.py              # Column mappings and constants
│   ├── data_processor.py      # Data cleaning and validation logic
│   ├── duplicate_checker.py   # Detects already-imported members by email
│   ├── member_importer.py     # Orchestrates the full import workflow
│   ├── sheet_reader.py        # Reads Excel files and Google Sheets
│   └── utils.py               # Shared utilities (logging, timestamps, etc.)
├── sample_data.csv            # Sample data file for testing
└── test_setup.py              # Verifies your installation is correct
```

