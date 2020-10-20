"""Main application file

 - Creates a mongo db client 
 - Defines a predictions persistence handler with the mongo db client and configures the prediction_api handler
 - Launches the prediction_api app using uvicorn 
"""

import uvicorn
from prediction_api import config as api_config
import mongo_db
import logging

# Define logger
logger = logging.getLogger(api_config.LOGGER_NAME + ".start_api" )

# Predictions persistance implemented as a Mongo database
db_client = None
try:
    db_client = mongo_db.MongoDBClient( host="localhost", 
                                        port=27017, 
                                        database_name="predictions_database", 
                                        collection_name="predictions_collection")
    logger.info("Mongo DB client connected OK")
except:
    db_client = None
    logger.warning("Mongo DB server connection FAIL")

def persistance_handler(documents):
    """Receives an iterable of documents persists them in the database"""
    if db_client: 
        db_client.insert_documents(documents)

# Set persistance handler in api
api_config.predictions_persistance_handler = persistance_handler

# Start application
if __name__ == "__main__":
    uvicorn.run("prediction_api.main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)
    