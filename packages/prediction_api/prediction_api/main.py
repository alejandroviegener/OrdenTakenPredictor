from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel

from prediction_model import config as model_config
from prediction_model import models
import pandas as pd

from datetime import datetime

from prediction_api.input_output_models import Features, Predictions
from prediction_api import utils 
from prediction_api import config as api_config


def persist_predictions(features_list, predictions):
    """Persist only if handler defined """

    if api_config.predictions_persistance_handler is None:
        return

    documents = []
    for features, prediction in zip(features_list, predictions):
        document = dict(features)
        document["prediction"] = float(prediction) 
        document["model_version"] = model_config.VERSION
        document["api_version"] = api_config.VERSION
        document["timestamp"] = str(datetime.now())

        documents.append(document)
        
    api_config.predictions_persistance_handler(documents)


# Api metadata, shown in documentation
tags_metadata = [
    {
        "name": "info",
        "description": "System info.",
    },
    {
        "name": "prediction",
        "description": "Request predictions given input features.",
    },
]

# Create app
app = FastAPI(  title="Order Taken Prediction",
                description="Predict the taken rate based on input features",
                version=api_config.VERSION,
                openapi_tags=tags_metadata)

# Load serialized model
model = models.LogisticRegressionClassifier.load(model_config.TRAINED_MODEL_FILE_PATH)


@app.get("/version", tags=["info"])
def read_version():
    return {"api_version": api_config.VERSION,
            "model_version": model_config.VERSION}

@app.post("/prediction/", response_model=Predictions, tags=["prediction"])
def request_prediction(features_list: List[Features]):

    # Convert input list to dataframe
    X = utils.features_list_to_dataframe(features_list)

    # Call prediction model
    predictions = model.predict(X, return_proba=False)

    # Insert predictions into database
    persist_predictions(features_list, predictions)

    # Return result
    return Predictions( predictions=list(predictions), 
                        model_version=model_config.VERSION,
                        api_version=api_config.VERSION)
