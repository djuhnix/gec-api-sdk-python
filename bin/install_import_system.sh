#!/bin/bash
# Installation script for GEC API Member Import System

set -e  # Exit on error

echo "=========================================="
echo "GEC API Member Import - Installation"
echo "=========================================="
echo ""

# Check Python version
echo "Checking Python version..."
python3 --version
echo ""

# Set up virtual environment
echo "Setting up virtual environment..."
if [ ! -d "venv" ] || [ ! -d ".venv" ]; then
    python3 -m venv .venv
    echo "✓ Created virtual environment in ./.venv"
else
    echo "✓ Virtual environment already exists in ./venv or ./.venv"
fi
echo ""

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt
echo ""

# Create .env if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "✓ Created .env file"
    echo "⚠ Please edit .env with your API credentials"
else
    echo "✓ .env file already exists"
fi
echo ""

# Test the setup
echo "Testing setup..."
python3 scripts/test_setup.py
echo ""

echo "=========================================="
echo "Installation complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Edit .env with your API credentials:"
echo "   nano .env"
echo ""
echo "2. Test with dry run:"
echo "   cd scripts"
echo "   python import_members.py --source excel --input sample_data.csv --dry-run"
echo ""
echo "3. Read the documentation:"
echo "   scripts/README.md - Full documentation"
echo "   scripts/QUICKSTART.md - Quick start guide"
echo ""

