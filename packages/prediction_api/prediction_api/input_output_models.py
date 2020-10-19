"""Defines input and outpus data Models"""

from typing import List
from pydantic import BaseModel, Field

# Define data schemas
class Features(BaseModel):
    to_user_distance: float = Field(..., gt=0, title="Distance (km) between store and user location")
    to_user_elevation: float = Field(..., gt=0, title="Difference in meters between the store and user altitude (m.a.s.l.)")
    total_earning: float = Field(..., gt=0, title="Courier earning by delivering the order")
    created_at: str = Field(..., title="Timestamp of order creation (Datetime compatible string)")

    def to_dict(self):
        return dict(self)


class Predictions(BaseModel):
    predictions: List[float] = Field(..., title="Predictions list")
    model_version: str = Field(..., title="model version number")
    api_version: str = Field(..., title="api version number")

