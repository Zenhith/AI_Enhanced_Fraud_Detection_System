"""
WSGI entry point for gunicorn.
This file imports the app variable from main.py.
"""

from main import app

# This allows gunicorn to find the application
application = app

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
