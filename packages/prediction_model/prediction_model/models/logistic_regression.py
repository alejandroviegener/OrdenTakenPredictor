
from prediction_model import preprocessing as pp
import pickle as pkl
from sklearn import pipeline
from sklearn import linear_model
from sklearn import metrics 
from prediction_model import config

# Globals 
SELECTED_FEATURES = ["to_user_distance", "to_user_elevation", "total_earning", "day_of_week", "time_of_day", "day_of_month"]
SCALED_FEATURES = ["to_user_distance", "to_user_elevation", "total_earning", "day_of_week", "time_of_day", "day_of_month"]
DATETIME_FEATURE = "created_at"
RANDOM_SEED = config.RANDOM_SEED
MAX_ITERS = 100
CLASS_WEIGTH = "balanced"


class LogisticRegressionClassifier():
    """Defines a logistic regression classifier"""

    def __init__(self):
        """Constructs a pipeline for logistic regression classifier"""
        
        self.estimators = [ ("date_time_features_creator", pp.CreateDateTimeFeatures(DATETIME_FEATURE)),
                            ("feature_selector", pp.FeatureSelector(SELECTED_FEATURES)),
                            ("standard_scaler", pp.StandardScaler(SCALED_FEATURES)),
                            ("predictor", linear_model.LogisticRegression(  random_state=RANDOM_SEED, 
                                                                            max_iter=MAX_ITERS, 
                                                                            class_weight=CLASS_WEIGTH))
                    ]
        self.pipe = pipeline.Pipeline(self.estimators)

    def fit(self, X, y):
        """Fit the pipeline to the data"""
        self.pipe.fit(X, y)
    
    def predict(self, X, return_proba=False):
        """Predict over new seen data"""
        
        if return_proba:
            return self.pipe.predict_proba(X)
        
        return self.pipe.predict(X)
    
    def performance_summary(self, X, y_true):
        """Get performance over dataset"""
        
        predicted = self.predict(X)

        performance = {}
        performance["accuracy"] = metrics.accuracy_score(y_true, predicted) 
        performance["precision"] = metrics.precision_score(y_true, predicted) 
        performance["roc_auc"] = metrics.roc_auc_score(y_true, predicted) 
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
