#!/bin/bash
set -e

echo "Starting deployment script..."

# Create virtual environment if it doesn't exist
if [ ! -d "/opt/venv" ]; then
  echo "Creating virtual environment..."
  python -m venv /opt/venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source /opt/venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

# List installed packages
echo "Installed packages:"
pip list

# Start the application
echo "Starting application..."
gunicorn --bind 0.0.0.0:$PORT app:server
