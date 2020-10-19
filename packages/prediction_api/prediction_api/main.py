from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel

from prediction_model import config as model_config
from prediction_model import models
import pandas as pd

from input_output_models import Features, Predictions
import utils 
import config as api_config


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
    pred = model.predict(X, return_proba=True)

    # Insert predictions into database
        # to-do

    # Return result
    return Predictions( predictions=list(pred), 
                        model_version=model_config.VERSION,
                        api_version=api_config.VERSION)
