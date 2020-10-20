"""Defines input and outpus data models for api validation
"""

from typing import List
from pydantic import BaseModel, Field
import datetime


# Define data schemas
class Features(BaseModel):
    """Defines the data model for the input features in the prediction model
    
    This model helps to validate the data send by the user to the api when a prediction is requested
    """

    order_id: int = Field(..., ge=0, title="Order identification number", example=145879)
    store_id: int = Field(..., ge=0, title="Store identification number", example=3000048)
    to_user_distance: float = Field(..., ge=0, title="Distance (km) between store and user location", example=1.2)
    to_user_elevation: float = Field(..., title="Difference in meters between the store and user altitude (m.a.s.l.)", example=230)
    total_earning: float = Field(..., gt=0, title="Courier earning by delivering the order", example=2000)
    created_at: datetime.datetime = Field(..., title="Timestamp of order creation (Datetime compatible string)", example="2019-09-15T23:52:45Z")

    def to_dict(self):
        return dict(self)
        

class Predictions(BaseModel):
    """Defines the data model response to a prediction request"""

    predictions: List[float] = Field(..., title="Predictions list")
    model_version: str = Field(..., title="model version number")
    api_version: str = Field(..., title="api version number")
