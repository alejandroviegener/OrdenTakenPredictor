"""Test the predictions api package"""

from fastapi.testclient import TestClient
from prediction_api.main import app
from prediction_api import config as api_config
from prediction_model import config as model_config
import pytest 


@pytest.fixture(scope="module")
def client():
    return TestClient(app)

def test_read_version(client):
    """Test version read"""

    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == { 'api_version': api_config.VERSION, 
                                'model_version': model_config.VERSION}

def test_request_predictions_valid_features(client):
    """Test request predictions with valid features"""

    # With valid features
    body_json = [   { 
                        "order_id": 0,
                        "store_id": 0,
                        "to_user_distance": 5,
                        "to_user_elevation": 500,
                        "total_earning": 1000,
                        "created_at": "2017-09-07T20:02:17Z"
                    },

                    { 
                        "order_id": 0,
                        "store_id": 0,
                        "to_user_distance": 1,
                        "to_user_elevation": 100,
                        "total_earning": 50000,
                        "created_at": "2017-09-07T20:02:17Z"
                    }]

    # When asked for predictions
    response = client.post("/prediction/", json=body_json)
    
    # Expect all OK
    assert response.status_code == 200
    assert response.json() == {'api_version': api_config.VERSION, 
                                'model_version':  model_config.VERSION, 
                                'predictions': [0, 1]}
    

@pytest.mark.parametrize("features",
                         [  {"to_user_distance": 1, "to_user_elevation": 300.4, "total_earning": -10.5, "created_at": "2017-09-07T20:02:17Z"},
                            {"to_user_distance": -1.2, "to_user_elevation": 300.4, "total_earning": 10.5, "created_at": "2017-09-07T20:02:17Z"},
                            {"to_user_distance": 0.5, "to_user_elevation": -100, "total_earning": 0, "created_at": "2017-09-07T20:02:17Z"},])
def test_request_predictions_invalid_features(client, features):
    """Test request predictions with invalid features"""

    # With invalid data
    body_json = [features]

    # When asking for predictions
    response = client.post("/prediction/", json=body_json)
    
    # Expect data validation error
    assert response.status_code == 422
    
