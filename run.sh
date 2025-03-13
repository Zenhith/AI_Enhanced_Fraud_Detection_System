#!/bin/bash

# Run the app directly if gunicorn is not available or fails
if command -v gunicorn &> /dev/null; then
    echo "Starting with gunicorn..."
    gunicorn --bind 0.0.0.0:${PORT:-8080} --workers=1 --threads=2 app:app
else
    echo "Gunicorn not found, starting with Python directly..."
    python app.py
fi
