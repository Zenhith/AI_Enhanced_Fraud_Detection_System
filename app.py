import os
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Log Python information
logger.info(f"Python version: {sys.version}")
logger.info(f"Python path: {sys.path}")

# Import Flask first to ensure it's correctly loaded
try:
    import flask
    logger.info(f"Flask version: {flask.__version__}")
except ImportError as e:
    logger.error(f"Failed to import Flask: {e}")
    sys.exit(1)

# Import Dash and related packages
try:
    import dash
    from dash import html, dcc
    import dash_bootstrap_components as dbc
    import plotly.express as px
    
    logger.info(f"Dash version: {dash.__version__}")
    logger.info(f"Successfully imported all Dash components")
except ImportError as e:
    logger.error(f"Failed to import Dash: {e}")
    sys.exit(1)

# Initialize the Dash app
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

# This is important for Railway deployment
if __name__ == "__main__":
    # Get port from environment (set by Railway)
    port = int(os.environ.get("PORT", 8050))
    logger.info(f"Starting Dash server on port {port}")
    
    # Run server with host set to 0.0.0.0 to make it externally visible
    app.run_server(debug=False, host='0.0.0.0', port=port)
