#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Check for Python installation
if ! command -v python3 &> /dev/null
then
    echo "Python is not installed. Please install Python before running this script."
    exit 1
fi

# Remove existing virtual environment if it exists
if [ -d "venv" ]; then
    rm -rf venv
fi

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

echo "Setup complete. To start the application, run 'source venv/bin/activate' and then 'python app.py'."
echo "Type 'Ctrl+C' and hit Enter to stop the application. Run 'deactivate' to stop the virtual environment."
