
import pytest
from prediction_model import preprocessing as pp
from prediction_model import utils
import pandas as pd
import numpy as np

def test_create_date_time_features():
    """Test date time transformation"""

    # With the dataset
    loader = utils.OrdersDataloader()
    X, _, _, _ = loader.get_train_test_split(0.25)
    
    # When a date time transformation is performed
    X = pp.CreateDateTimeFeatures(loader.date_time_column).fit_transform(X)

    # Check that all is OK
    assert all([a in X.columns for a in pp.CreateDateTimeFeatures.created_features])


def test_feature_selector():
    """Test feature selector"""

    # With the dataset and the original columns
    loader = utils.OrdersDataloader()
    X, _, _, _ = loader.get_train_test_split(0.25)
    original_columns = X.columns
    
    # When some features are selected 
    selected_columns = original_columns[0:2]
    dropped_columns = original_columns[2:-1]
    X = pp.FeatureSelector(selected_columns).fit_transform(X)

    # Check that only the selected columns are left
    actual_columns = X.columns
    print(original_columns)
    print(actual_columns)
    assert all([a in actual_columns for a in selected_columns])
    assert all([a not in actual_columns for a in dropped_columns])


def test_feature_dropper():
    """Test feature dropper"""

    # With the dataset and the original columns
    loader = utils.OrdersDataloader()
    X, _, _, _ = loader.get_train_test_split(0.25)
    original_columns = X.columns
    
    # When some features are dropped 
    selected_columns = original_columns[0:2]
    dropped_columns = original_columns[2:-1]
    X = pp.FeatureDropper(dropped_columns).fit_transform(X)

    # Check that only the non dropped columns are left
    actual_columns = X.columns
    print(original_columns)
    print(actual_columns)
    assert all([a in actual_columns for a in selected_columns])
    assert all([a not in actual_columns for a in dropped_columns])


def test_standard_scaler():

    # With a toy dataframe
    X = pd.DataFrame({  "c1": [1, 2, 3, 40], 
                        "c2": [100, 100, 100, 200],
                        "c3": [23, 24, 25, 106]
                        })

    # When standard scaling
    X = pp.StandardScaler(["c1", "c3"]).fit_transform(X)

    # Check that the specified columns where scaled
    mean_values = X.mean()
    deviation_values = X.std()
    assert np.isclose( mean_values[0],  0)
    assert np.isclose( mean_values[1],  np.mean([100, 100, 100, 200]))
    assert np.isclose( mean_values[2],  0)
    assert deviation_values[0] < 2
    assert deviation_values[1] > 2
    assert deviation_values[2] < 2
