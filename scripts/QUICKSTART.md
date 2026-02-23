# Quick Start — Member Import

This guide gets you from zero to your first import in 5 steps.
For full documentation, see [README.md](README.md).

---

## Step 1 — Install dependencies

Open a terminal in the **project root** (not the `scripts/` folder):

```bash
# Create an isolated Python environment (only needed once)
python3 -m venv .venv

# Activate it (do this every time you open a new terminal)
source .venv/bin/activate       # macOS / Linux
# .venv\Scripts\activate        # Windows

# Install packages
pip install -r requirements.txt
pip install -e .
```

Your prompt will show `(.venv)` when the environment is active.

---

## Step 2 — Configure your credentials

```bash
cp .env.example .env
```

Open `.env` in any text editor and set:

```env
GEC_API_HOST=http://localhost:8080   # URL of the API server
GEC_API_TOKEN=eyJhbGci...            # Your JWT token (ask your admin)
```

---

## Step 3 — Verify the setup

```bash
cd scripts
python3 test_setup.py
```

If everything is green, you're ready to import.

---

## Step 4 — Dry run with your file

Always validate your data first — this checks for errors without touching the database:

```bash
python3 import_members.py --source excel --input ../data/members.xlsx --dry-run
```

Read the output. If records show validation errors, fix them in your file and repeat.

---

## Step 5 — Run the real import

```bash
python3 import_members.py --source excel --input ../data/members.xlsx
```

When it finishes, you'll see a summary:

```
==================================================
IMPORT SUMMARY
==================================================
Total Records:     100
Success:            95
Failed:              5
Duplicates:          0
==================================================
Failed records saved to: failed_imports_20260223_182700.xlsx
==================================================
```

Failed records are saved to an Excel file. Fix the errors in that file and re-import it.

---

## Common commands

```bash
# Show all available options
python3 import_members.py --help

# Import from Google Sheets (OAuth2 — opens a browser to authorize)
python3 import_members.py \
    --source gsheet \
    --input "https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID" \
    --auth-method oauth2 \
    --credentials-path ../credentials.json

# Save failures to a specific path
python3 import_members.py --source excel --input data.xlsx \
    --output-failed my_failures.xlsx

# Show detailed logs (useful when something goes wrong)
python3 import_members.py --source excel --input data.xlsx --log-level DEBUG

# Stop at the first error instead of continuing
python3 import_members.py --source excel --input data.xlsx --stop-on-error
```

---

## Something went wrong?

| Symptom | Fix |
|---|---|
| `No module named '...'` | Run `pip install -r requirements.txt && pip install -e .` with the venv active |
| `401 Unauthorized` | Your token is invalid or expired — update `GEC_API_TOKEN` in `.env` |
| `Connection refused` | Check `GEC_API_HOST` in `.env` and that the server is running |
| Column not recognized | Check the column name against the [Column Reference](README.md#column-reference) |
| Validation errors | Run with `--dry-run --log-level DEBUG` to see what the script sees |

See [README.md — Troubleshooting](README.md#troubleshooting) for more.


