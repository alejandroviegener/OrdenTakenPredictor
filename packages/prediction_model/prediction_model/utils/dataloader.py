"""Utility class to load the dataset"""

import pandas as pd
from prediction_model import config
from sklearn import model_selection

# Globals
RANDOM_SEED = config.RANDOM_SEED 
ORDERS_DATASET_FILE_PATH = config.DATASET_FILE_PATH
DATE_TIME_COLUMN = "created_at"


class OrdersDataloader():
    """Loads the orders dataset.
    
    Typical usage:
        loader = OrdersDataloader()
        X_train, X_test, y_train, y_test = loader.get_train_test_split(0.25)
    """

    # Globals
    date_time_column = DATE_TIME_COLUMN

    def __init__(self):
        """Initialized a dataframe by reading the csv file"""

        # Read dataframe
        df = pd.read_csv(ORDERS_DATASET_FILE_PATH)
        
        # Convert created_at column to date time object
        df[DATE_TIME_COLUMN] = pd.to_datetime(df[DATE_TIME_COLUMN])   

        # Filter outliers detected in research phase
        filter_elevation = (df["to_user_elevation"] < 600) 
        filter_earnings = (df["total_earning"] < 40000) & (df["total_earning"] > 0)
        filter_distance = df["to_user_distance"] < 8
        df = df[filter_elevation & filter_earnings & filter_distance]

        self.data = df

    def get_train_test_split(self, test_size):
        """Loads the data from a csv file and returns a train, test split
        
            Returns (X_train, X_test, y_train, y_test)
        """

        # Return train and test sets
        X = self.data.copy()
        labels = X["taken"]
        features = X.drop(columns=["taken"])
        split = model_selection.train_test_split(   features, 
                                                    labels, 
                                                    test_size = test_size, 
                                                    stratify=labels, 
                                                    random_state=RANDOM_SEED)
        return split
                                                                            