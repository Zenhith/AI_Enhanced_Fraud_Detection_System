import os
import logging
import threading
import sys
from datetime import datetime

# Configure logging (directly to console for Railway)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Import core dash and flask dependencies
import dash
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go

# Create a simple dashboard for initial deployment
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
app.title = "AI Fraud Intelligence Dashboard"

# Create a basic layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("AI Fraud Intelligence Dashboard", className="my-4 text-center"),
            html.P("Simplified version for initial deployment", className="text-center"),
            
            dbc.Card([
                dbc.CardHeader("System Status"),
                dbc.CardBody([
                    html.H5("Successfully Deployed", className="text-success"),
                    html.P("The system has been deployed successfully. This is a simplified version for initial deployment."),
                    html.P("Environment: " + os.environ.get("RAILWAY_ENVIRONMENT", "Development")),
                    html.P("Port: " + os.environ.get("PORT", "8050")),
                    html.P("Time: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                ])
            ], className="mb-4"),
            
            dbc.Card([
                dbc.CardHeader("Next Steps"),
                dbc.CardBody([
                    html.P("Now that the basic application is deployed, you can:"),
                    html.Ul([
                        html.Li("Gradually add back the advanced features"),
                        html.Li("Connect to a persistent database"),
                        html.Li("Add data collection functionality"),
                        html.Li("Implement the full dashboard")
                    ])
                ])
            ])
        ], width=12)
    ])
], fluid=True)

# Set up the server
server = app.server

if __name__ == "__main__":
    # Get the port from the environment (Railway sets this)
    port = int(os.environ.get("PORT", 8050))
    
    # Log deployment information
    logger.info(f"Starting server on port {port}")
    logger.info(f"Environment: {os.environ.get('RAILWAY_ENVIRONMENT', 'Development')}")
    
    # Run the server
    app.run_server(debug=False, host='0.0.0.0', port=port)
