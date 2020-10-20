"""Tests the mongo_db module"""

import pytest 
import mongo_db


def test_server_connection_error():
    """Test exception raise if server connection error"""

    with pytest.raises(Exception):
        mongo_db.MongoDBClient( host="0.0.0.0", 
                                port=4789, 
                                database_name="",
                                collection_name=""
                )
                