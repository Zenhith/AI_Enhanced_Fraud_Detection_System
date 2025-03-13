# Import necessary modules and classes
import os
import logging
import threading
import sys
from datetime import datetime

# Import from your main source code file
from fds import (
    RealTimeDataIngestionManager, 
    HistoricalDataCollector, 
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

# Skip seeding sample data - we only want real-time collection
# seed_sample_data(data_manager)  # Commented out

# Create dashboard
dashboard = EnhancedAIFraudDashboard(data_manager)
setup_multi_page_dashboard(dashboard, data_manager)

# Connect dashboard to data manager
data_manager.dashboard = dashboard

# Export the Dash app for gunicorn to serve
# For Dash apps, the correct WSGI app is the 'server' attribute
app = dashboard.app
server = app.server  # This is what gunicorn should use

def main():
    """
    Main function to run the AI Fraud Detection System
    """
    try:
        print("Starting AI Fraud Detection System...")
        
        # Start real-time data collection immediately
        print("Starting immediate data collection...")
        # Collect data once before starting the thread
        data_manager.collect_data()
        
        # Start periodic collection in a separate thread
        print("Starting periodic data collection thread...")
        collection_thread = threading.Thread(
            target=data_manager.start_periodic_collection,
            kwargs={'collection_interval_minutes': 15},
            daemon=True
        )
        collection_thread.start()
        
        # Get port from environment or use default
        port = int(os.environ.get('PORT', 8050))
        
        # Start dashboard in main thread
        print(f"Starting dashboard at http://localhost:{port}")
        print("Press Ctrl+C to stop the server")
        dashboard.run(debug=False, host='0.0.0.0', port=port)
        
    except Exception as e:
        logger.error(f"Critical error in AI Fraud Detection System: {e}")
        import traceback
        traceback.print_exc()

# Add this block to run the script directly
if __name__ == "__main__":
    import sys
    
    # Check if we're running in historical mode
    if len(sys.argv) > 1 and sys.argv[1] == "--historical":
        print("Running in historical data collection mode")
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s: %(message)s',
            handlers=[
                logging.FileHandler('historical_collection.log'),
                logging.StreamHandler()
            ]
        )
        logger = logging.getLogger(__name__)
        
        try:
            # Run historical collection
            historical_collector = HistoricalDataCollector(data_manager)
            collected = historical_collector.collect_historical_data()
            
            print(f"Successfully collected {collected} historical reports")
            sys.exit(0)
        
        except Exception as e:
            logger.error(f"Error in historical collection: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)
    else:
        # Run normal main function
        main()
