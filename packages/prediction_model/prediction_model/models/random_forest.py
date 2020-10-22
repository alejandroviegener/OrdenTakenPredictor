"""This module defines a random forest model for the order taken prediction

Typical usage:

  - Fit:

    # Get the dataset data 
    data = utils.OrdersDataloader().get_train_test_split(TEST_SIZE)
    X_train, _, y_train, _ = data

    # Fit the model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Save the model
    model.save(TRAINED_MODEL_FILE_PATH)

  - The model can be directly loaded using the load class method:

    loaded_model = RandomForestClassifier.load(model_config.TRAINED_MODEL_FILE_PATH)
"""

from prediction_model import preprocessing as pp
import pickle as pkl
from sklearn import pipeline
from sklearn import ensemble
from sklearn import metrics 
from prediction_model import config
import numpy as np
from prediction_model import config
import logging

# Globals 
SELECTED_FEATURES = ["to_user_distance", "to_user_elevation", "total_earning", "day_of_week", "time_of_day", "day_of_month"]
DATETIME_FEATURE = "created_at"
RANDOM_SEED = config.RANDOM_SEED

# Define module logger
logger = logging.getLogger(config.LOGGER_NAME + ".random_forest")


class RandomForestClassifier():
    """Defines a lrandom forest classifier

    The model can be pickled and the reloaded from the serialized file
    """

    def __init__(self):
        """Constructs a pipeline for logistic regression classifier"""
        
        self.estimators = [ ("date_time_features_creator", pp.CreateDateTimeFeatures(DATETIME_FEATURE)),
                            ("feature_selector", pp.FeatureSelector(SELECTED_FEATURES)),
                            ("predictor", ensemble.RandomForestClassifier(  random_state=RANDOM_SEED, 
                                                                            n_estimators=131, 
                                                                            min_samples_split=100, 
                                                                            min_samples_leaf=2,
                                                                            max_depth=50, 
                                                                            class_weight="balanced", 
                                                                            max_leaf_nodes=200, 
                                                                            max_features="sqrt"))
                ]
        self.pipe = pipeline.Pipeline(self.estimators)

    def fit(self, X, y):
        """Fit the pipeline to the data
        Args:
            X: dataframe with the the input features
            y: array of 1 and 0s  
        """
        self.pipe.fit(X, y)
    
    def predict(self, X, return_proba=False):
        """Predict over new seen data
        
        Set return_proba to True to return the 1 probability 
        """
        
        logger.info("Predictions pipeline update")

        if return_proba:
            return np.round(self.pipe.predict_proba(X)[:, 1], decimals=4)
        
        return self.pipe.predict(X)
    
    def performance_summary(self, X, y_true):
        """Get performance over dataset
        
        Returns the accuracy, precision, roc_auc, f1_socre, recalll and the confusion matrix
        """
        
        predicted = self.predict(X)

        performance = {}
        performance["accuracy"] = metrics.accuracy_score(y_true, predicted) 
        performance["precision"] = metrics.precision_score(y_true, predicted) 
        performance["roc_auc"] = metrics.roc_auc_score(y_true, predicted) 
        performance["f1_score"] = metrics.f1_score(y_true, predicted) 
        performance["recall"] = metrics.recall_score(y_true, predicted) 
        performance["confusion_matrix"] = metrics.confusion_matrix(y_true, predicted) 

        return performance

    @classmethod
    def load(cls, file):
        """Initialize a classifier from a serialized object"""
        
        with open(file, 'rb') as handle:
            obj = pkl.load(handle)

        return obj

    def save(self, file):
        """Serialize the pipeline"""

        with open(file, 'wb') as handle:
            pkl.dump(self, handle)    
