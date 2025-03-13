import os
import sys
import logging
import subprocess

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

logger.info("Starting application initialization")
logger.info(f"Python version: {sys.version}")
logger.info(f"Python executable: {sys.executable}")
logger.info(f"Current directory: {os.getcwd()}")
logger.info(f"Files in directory: {os.listdir('.')}")

# Verify Dash installation
try:
    # Run pip show dash to verify it's installed
    result = subprocess.run([sys.executable, "-m", "pip", "show", "dash"], 
                           capture_output=True, text=True)
    logger.info(f"Dash package info:\n{result.stdout}")
    
    # If dash is not found, try to install it again
    if "not found" in result.stderr or result.returncode != 0:
        logger.warning("Dash not found, attempting to install...")
        install_result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "dash==2.9.3"], 
            capture_output=True, text=True)
        logger.info(f"Install result: {install_result.stdout}")
        logger.info(f"Install error: {install_result.stderr}")
except Exception as e:
    logger.error(f"Error checking Dash installation: {e}")

# Try to import Flask
try:
    from flask import Flask
    logger.info("Successfully imported Flask")
    
    # Create a Flask app as fallback
    flask_app = Flask(__name__)
    
    @flask_app.route('/')
    def home():
        return """
        <html>
            <head><title>Dash Import Issue</title></head>
            <body>
                <h1>Import Error</h1>
                <p>We're encountering an issue importing Dash. See logs for details.</p>
                <p>This fallback Flask app is working, so the server is running.</p>
            </body>
        </html>
        """
except ImportError as e:
    logger.error(f"Failed to import Flask: {e}")
    sys.exit(1)

# Try to import Dash
try:
    import dash
    from dash import html, dcc
    import dash_bootstrap_components as dbc
    logger.info(f"Successfully imported Dash version {dash.__version__}")
    
    # Create Dash app
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
    server = app.server  # This is the Flask server
    
    # Create layout
    app.layout = html.Div([
        html.H1("Dash App Successfully Deployed"),
        html.P("If you can see this, Dash is working correctly!"),
        dcc.Graph(
            figure={
                'data': [{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Test'}],
                'layout': {'title': 'Basic Dash Graph'}
            }
        )
    ])
    
except ImportError as e:
    logger.error(f"Failed to import Dash: {e}")
    logger.info("Falling back to Flask-only app")
    server = flask_app

# This ensures we have a 'server' variable for gunicorn regardless
if 'server' not in locals():
    logger.warning("server variable not set, using flask_app")
    server = flask_app

# Entry point for the app when run directly
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    logger.info(f"Starting server on port {port}")
    
    # Determine which app to run
    if 'app' in locals():
        logger.info("Running Dash app")
        app.run_server(debug=False, host='0.0.0.0', port=port)
    else:
        logger.info("Running Flask app")
        server.run(host='0.0.0.0', port=port)
