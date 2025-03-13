"""
WSGI entry point for gunicorn.
This file imports the app variable from main.py and ensures it's a proper WSGI application.
"""

from main import app

# This allows gunicorn to find the application
# For Dash apps, the 'server' attribute is the WSGI application
application = app.server

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
