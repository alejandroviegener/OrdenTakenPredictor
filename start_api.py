
import uvicorn
from prediction_api import config as api_config
import mongo_db


# Predictions persistance implemented as a Mongo database
db_client = None
try:
    db_client = mongo_db.MongoDBClient( host="localhost", 
                                        port=27017, 
                                        database_name="predictions_database", 
                                        collection_name="predictions_collection")
    print("Server found ------------------------")
except:
    db_client = None
    print("Server NOT found ------------------------")

def persistance_handler(documents):
    """Receives an iterable of documents persists them in the database"""
    if db_client: 
        print("Persisting predctions ---------------------", documents)
        db_client.insert_documents(documents)

# Set persistance handler in api
api_config.predictions_persistance_handler = persistance_handler

# Start application
if __name__ == "__main__":
    uvicorn.run("prediction_api.main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)