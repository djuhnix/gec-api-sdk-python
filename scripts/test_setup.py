#!/usr/bin/env python3
"""
Simple test script to verify the import system is set up correctly.
"""

import sys
from pathlib import Path

# Add scripts directory to path
scripts_dir = Path(__file__).parent
sys.path.insert(0, str(scripts_dir))

def test_imports():
    """Test that all modules can be imported."""
    print("Testing module imports...")

    try:
        from scripts.helpers import config
        print("✓ config module imported")
    except Exception as e:
        print(f"✗ Error importing config: {e}")
        return False

    try:
        from scripts.helpers import utils
        print("✓ utils module imported")
    except Exception as e:
        print(f"✗ Error importing utils: {e}")
        return False

    try:
        from scripts.helpers import data_processor
        print("✓ data_processor module imported")
    except Exception as e:
        print(f"✗ Error importing data_processor: {e}")
        return False

    try:
        from scripts.helpers import sheet_reader
        print("✓ sheet_reader module imported")
    except Exception as e:
        print(f"✗ Error importing sheet_reader: {e}")
        return False

    try:
        from scripts.helpers import duplicate_checker
        print("✓ duplicate_checker module imported")
    except Exception as e:
        print(f"✗ Error importing duplicate_checker: {e}")
        return False

    try:
        from scripts.helpers import member_importer
        print("✓ member_importer module imported")
    except Exception as e:
        print(f"✗ Error importing member_importer: {e}")
        return False

    return True

def test_dependencies():
    """Test that required dependencies are installed."""
    print("\nTesting dependencies...")

    dependencies = [
        'pandas',
        'openpyxl',
        'gspread',
        'google.auth',
        'google_auth_oauthlib',
        'dotenv',
        'gec_api_sdk'
    ]

    all_ok = True
    for dep in dependencies:
        try:
            __import__(dep)
            print(f"✓ {dep} is installed")
        except ImportError:
            print(f"✗ {dep} is NOT installed")
            all_ok = False

    return all_ok

def main():
    """Run tests."""
    print("=" * 60)
    print("GEC API Member Import - System Test")
    print("=" * 60)

    modules_ok = test_imports()
    deps_ok = test_dependencies()

    print("\n" + "=" * 60)
    if modules_ok and deps_ok:
        print("✓ All tests passed!")
        print("=" * 60)
        print("\nYou can now use the import script:")
        print("  python import_members.py --help")
        return 0
    else:
        print("✗ Some tests failed")
        print("=" * 60)
        if not deps_ok:
            print("\nInstall missing dependencies:")
            print("  pip install -r requirements.txt")
        return 1

if __name__ == '__main__':
    sys.exit(main())

