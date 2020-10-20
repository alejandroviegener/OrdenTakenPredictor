import pymongo 

SERVER_CONNECTION_TIMEOUT_MS = 2000

class MongoDBClient:
    """"Client abstraction for mongo db"""

    def __init__(self, database_name, collection_name, host="0.0.0.0", port=27017, username=None, password=None):
        """Initialize database client"""
        
        self.host = host
        self.port = port
        self.database = database_name
        self.collection = collection_name
        self.username = username
        self.password = password

        try:
            # Create client
            self.client = pymongo.MongoClient(  host, 
                                                port, 
                                                serverSelectionTimeoutMS=SERVER_CONNECTION_TIMEOUT_MS, 
                                                username=username, 
                                                password=password
                            )
            
            # Check connection
            self.client.admin.command("ismaster")

            # Create database and collection
            self.database = self.client[database_name]
            self.collection = self.database[collection_name]

        # Raise exception if no connection
        except Exception as exception:
            raise exception
    
    def insert_document(self, document):
        """Insert one document into the db and returns the _id inserted"""
        return self.collection.insert_one(document)

    def insert_documents(self, documents):
        """Insert an iterable of documents"""
        return self.collection.insert_many(documents)

