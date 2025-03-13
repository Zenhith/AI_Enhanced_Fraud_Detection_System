import os
import logging
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.express as px

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
server = app.server  # Expose Flask server for deployment

# Create a simple layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("AI Fraud Intelligence Dashboard", className="text-center my-4"),
            html.P("Initial deployment - minimal version", className="text-center text-secondary"),
            
            dbc.Card([
                dbc.CardHeader("Deployment Status"),
                dbc.CardBody([
                    html.H4("Successfully Deployed!", className="text-success"),
                    html.P("This is a minimal version to verify deployment works correctly."),
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

# Entry point for the application
if __name__ == "__main__":
    # Get port from environment (set by Railway)
    port = int(os.environ.get("PORT", 8050))
    logger.info(f"Starting server on port {port}")
    
    # Run server
    app.run_server(debug=False, host='0.0.0.0', port=port)
