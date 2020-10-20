"""Implements a mongo database client, that enables to connect and write to ir

Typical usage:

client = MongoDBClient( database_name="test_db",
                        collection_name="test_collection",
                        host="0.0.0.0",
                        port=27017)
test_document = {"a": 12, "b": 43}
client.insert_document(test_document)

"""

import pymongo 

# Connection tiemout
SERVER_CONNECTION_TIMEOUT_MS = 2000

class MongoDBClient:
    """"Client abstraction for mongo db"""

    def __init__(self, database_name, collection_name, host="0.0.0.0", port=27017, username=None, password=None):
        """Initialize database client
        
        Args:
            database_name: name of the database to connect to. It is created if no exists
            collection_name: name of the collection in the db
            host: string indicating the host
            port: port number
            username: default is None
            password: default is None

        Raises:
            Exception if server connection timeout
        """
        
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

