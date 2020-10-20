import pytest 
import mongo_db


def test_server_connection():
    """Test exception raise if server not connected"""

    with pytest.raises(Exception):
        mongo_db.MongoDBClient( host="0.0.0.0", 
                                port=4789, 
                                database_name="",
                                collection_name=""
                )
                