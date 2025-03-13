#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

echo "Starting build process..."

# Print Python version
python --version

# Upgrade pip
python -m pip install --upgrade pip
echo "Upgraded pip"

# Install packages one by one
echo "Installing Flask..."
pip install flask==2.2.3

echo "Installing Gunicorn..."
pip install gunicorn==20.1.0

echo "Installing Dash..."
pip install dash==2.9.3

echo "Installing Dash components..."
pip install dash-bootstrap-components==1.4.0
pip install dash-html-components==2.0.0
pip install dash-core-components==2.0.0
pip install dash-table==5.0.0

echo "Installing Plotly..."
pip install plotly==5.14.0

# List installed packages
echo "Installed packages:"
pip freeze

echo "Build completed successfully."
