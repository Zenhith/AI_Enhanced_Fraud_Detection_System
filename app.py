import os
import logging
import sys
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

# Import the main modules
from fds import (
    RealTimeDataIngestionManager, 
    seed_sample_data, 
    EnhancedAIFraudDashboard,
    add_novelty_detection_page
)

# Railway will provide a PORT environment variable
port = int(os.environ.get("PORT", 8050))

# Create and initialize the application
def create_app():
    try:
        # Create data ingestion manager
        logger.info("Initializing data manager...")
        data_manager = RealTimeDataIngestionManager(
            database_path='ai_fraud_reports.db'
        )
        
        # Initialize database with default data
        logger.info("Initializing database...")
        data_manager.initialize_database()
        
        # Pre-seed database with sample data if needed
        logger.info("Seeding sample data...")
        seed_sample_data(data_manager)
        
        # Create dashboard
        logger.info("Setting up dashboard...")
        dashboard = EnhancedAIFraudDashboard(data_manager)
        
        # Add novelty detection page
        logger.info("Setting up novelty detection...")
        add_novelty_detection_page(dashboard, data_manager)
        
        # Connect dashboard to data manager
        data_manager.dashboard = dashboard
        
        return dashboard.app.server
    
    except Exception as e:
        logger.error(f"Critical error in app initialization: {e}")
        import traceback
        traceback.print_exc()
        raise

# Create the Flask app
app = create_app()

# This is the entry point for Railway
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
