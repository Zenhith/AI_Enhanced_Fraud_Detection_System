import os
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# Log environment info
logger.info(f"Python version: {sys.version}")
logger.info(f"Python executable: {sys.executable}")
logger.info(f"Environment variables: PORT={os.environ.get('PORT', 'not set')}")

# First, try to import Flask
try:
    from flask import Flask, render_template_string
    logger.info("Successfully imported Flask")
except ImportError as e:
    logger.error(f"Failed to import Flask: {e}")
    sys.exit(1)

# Then, try to import Dash
try:
    import dash
    from dash import html, dcc
    import dash_bootstrap_components as dbc
    import plotly.express as px
    
    logger.info(f"Successfully imported Dash version {dash.__version__}")
    
    # Create Dash app
    app = dash.Dash(__name__, 
                   external_stylesheets=[dbc.themes.DARKLY],
                   suppress_callback_exceptions=True)
    
    # Make server available for gunicorn
    server = app.server
    
    # Create a simple layout
    app.layout = dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H1("AI Fraud Intelligence Dashboard", className="text-center my-4"),
                html.P("Basic Dash deployment version", className="text-center text-secondary"),
                
                dbc.Card([
                    dbc.CardHeader("Deployment Status"),
                    dbc.CardBody([
                        html.H4("Successfully Deployed!", className="text-success"),
                        html.P("This is a basic version to verify Dash deployment works correctly."),
                        html.P(f"Running on port: {os.environ.get('PORT', '8050')}")
                    ])
                ], className="mb-4"),
                
                # Simple demo chart
                dbc.Card([
                    dbc.CardHeader("Sample Visualization"),
                    dbc.CardBody([
                        dcc.Graph(
                            figure=px.bar(
                                x=["Deepfake", "Voice Cloning", "AI Phishing", "Identity Theft", "Financial Fraud"],
                                y=[35, 25, 40, 20, 30],
                                title="Sample AI Fraud Categories",
                                labels={"x": "Category", "y": "Incidents"}
                            )
                        )
                    ])
                ])
            ], width=12)
        ])
    ], fluid=True)
    
    logger.info("Dash app created successfully")
    
except ImportError as e:
    logger.error(f"Failed to import Dash: {e}")
    logger.info("Creating Flask-only app as fallback")
    
    # Create a basic Flask app as fallback
    app = Flask(__name__)
    server = app
    
    @app.route('/')
    def home():
        return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Flask Fallback</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; }
                .container { max-width: 800px; margin: 0 auto; }
                .card { border: 1px solid #ddd; border-radius: 8px; padding: 20px; margin-bottom: 20px; }
                .warning { color: orange; }
                h1 { color: #333; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>AI Fraud Intelligence Dashboard</h1>
                <p>Flask fallback version</p>
                
                <div class="card">
                    <h2 class="warning">Dash Import Failed</h2>
                    <p>The application is running with Flask only because Dash could not be imported.</p>
                    <p>This confirms that the server is running, but we need to fix the Dash installation.</p>
                </div>
            </div>
        </body>
        </html>
        """)

if __name__ == "__main__":
    # Get port from environment
    port = int(os.environ.get("PORT", 8050))
    logger.info(f"Starting server on port {port}")
    
    # Run the appropriate app
    if 'app' in locals() and hasattr(app, 'run_server'):
        # Run Dash app
        app.run_server(debug=False, host='0.0.0.0', port=port)
    elif 'server' in locals():
        # Run Flask app
        server.run(host='0.0.0.0', port=port)
    else:
        logger.error("No app to run!")
        sys.exit(1)
