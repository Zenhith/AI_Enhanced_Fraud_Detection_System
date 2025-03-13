import os
import logging
from fds import (
    RealTimeDataIngestionManager, 
    seed_sample_data, 
    EnhancedAIFraudDashboard, 
    setup_multi_page_dashboard 
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler('ai_fraud_detection.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Create data ingestion manager
data_manager = RealTimeDataIngestionManager(
    database_path='ai_fraud_reports.db'
)

# Initialize database with default data
data_manager.initialize_database()

# Pre-seed database with sample data
seed_sample_data(data_manager)

# Create dashboard
dashboard = EnhancedAIFraudDashboard(data_manager)

# Setup multi-page dashboard
setup_multi_page_dashboard(dashboard, data_manager)

# Connect dashboard to data manager
data_manager.dashboard = dashboard

# Export the Dash app for gunicorn to serve
app = dashboard.app

# Set port for Dash app
port = int(os.environ.get('PORT', 8080))

if __name__ == "__main__":
    # Start dashboard
    print(f"Starting dashboard at http://0.0.0.0:{port}")
    dashboard.run(debug=False, host='0.0.0.0', port=port)
