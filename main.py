# Import necessary modules and classes
import os
import logging
import threading
import sys
from datetime import datetime

# Import from your main source code file
from fds import (
    RealTimeDataIngestionManager, 
    seed_sample_data, 
    HistoricalDataCollector, 
    EnhancedAIFraudDashboard, 
    add_novelty_detection_page
)

def main():
    """
    Main function to run the AI Fraud Detection System
    """
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s: %(message)s',
        handlers=[
            logging.StreamHandler()  # Only log to stdout for Railway
        ]
    )
    logger = logging.getLogger(__name__)

    try:
        print("Starting AI Fraud Detection System...")
        
        # Create data ingestion manager
        print("Initializing data manager...")
        data_manager = RealTimeDataIngestionManager(
            database_path='ai_fraud_reports.db'
        )
        
        # Initialize database with default data
        print("Initializing database...")
        data_manager.initialize_database()
        
        # Pre-seed database with sample data if needed
        print("Seeding sample data...")
        seed_sample_data(data_manager)
        
        # Create dashboard
        print("Setting up dashboard...")
        dashboard = EnhancedAIFraudDashboard(data_manager)
        
        print("Setting up novelty detection...")
        add_novelty_detection_page(dashboard, data_manager) 
        
        # Connect dashboard to data manager
        data_manager.dashboard = dashboard
        
        # Start data collection in a separate thread
        print("Starting data collection thread...")
        collection_thread = threading.Thread(
            target=data_manager.start_periodic_collection,
            kwargs={'collection_interval_minutes': 15, 'forecast_interval_hours': 6},
            daemon=True
        )
        collection_thread.start()
        
        # Get port from environment variable (Railway sets this automatically)
        port = int(os.environ.get("PORT", 8050))
        host = '0.0.0.0'  # Listen on all interfaces
        
        # Start dashboard in main thread
        print(f"Starting dashboard on {host}:{port}")
        dashboard.app.run_server(debug=False, host=host, port=port)
        
    except Exception as e:
        logger.error(f"Critical error in AI Fraud Detection System: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

# Add this block to run the script directly
if __name__ == "__main__":
    # Run normal main function
    main()
