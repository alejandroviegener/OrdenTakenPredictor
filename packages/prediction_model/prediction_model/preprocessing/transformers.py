"""
Defines custom transformers as derived classed of the sklearn base transformer
This enables to use this custom transformers as part of a sklearn pipeline

Example:

    feature_dropper = FeatureDropper(["col_name_1", "col_name_2"])
    feature_dropper.fit_transform(X)
"""

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn import preprocessing as pp
import pandas as pd


class FeatureDropper(BaseEstimator, TransformerMixin):
    """Drops columns from a dataframe"""

    def __init__(self, column_names=None):
        """Initializes the class with the columns to drop from the dataframe"""
        
        self.column_names = column_names

    def  fit(self, X, y=None):
        return self

    def transform(self, X):
        """Drops the columns passed during instance init"""

        X = X.copy()
        for column_name in self.column_names:
            X.drop(columns=column_name, inplace=True)

        return X


class FeatureSelector(BaseEstimator, TransformerMixin):
    """Selects columns from a dataframe"""

    def __init__(self, column_names=None):
        """Initializes the class with the columns to select from the dataframe"""
        
        self.column_names = column_names

    def  fit(self, X, y=None):
        return self

    def transform(self, X):
        """Drops the columns passed during instance init"""

        X = X.copy()
        X = X[self.column_names]

        return X


class StandardScaler(BaseEstimator, TransformerMixin):
    """Standard scales a set of defined columns"""

    def __init__(self, column_names):
        """Inititalizes the class with the columns to scale"""

        # Columns to scale
        self.column_names = column_names

        # Create dictionary of scalers
        self.scalers = {column_name: pp.StandardScaler() for column_name in self.column_names}
        
    def fit(self, X, y=None):
        """Fits every scalar"""

        X = X.copy()
        for column_name, scaler in self.scalers.items():
            scaler.fit(X[[column_name]])    

        return self

    def transform(self, X):
        """Applies the transformation fitted to new data"""

        X = X.copy()
        for column_name, scaler in self.scalers.items():
            X[column_name] = scaler.transform(X[[column_name]])

        return X

    
class CreateDateTimeFeatures(BaseEstimator, TransformerMixin):
    """Create date time features from datetime column"""

    # Class attribute
    created_features = ["day_of_week", "time_of_day", "month", "day_of_month"]

    def __init__(self, datetime_column_name):
        """Receives the origin datetime and creates the features passed"""

        self.datetime_column_name = datetime_column_name

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        """Extract datetime info from datetime object"""
        
        X = X.copy()
        X[self.datetime_column_name] = pd.to_datetime(X[self.datetime_column_name])
        datetime = X[self.datetime_column_name].dt
        
        X["day_of_week"] = datetime.dayofweek
        X["time_of_day"] = datetime.hour + datetime.minute / 60
        X["month"] = datetime.month
        X["day_of_month"] = datetime.day

        return X
