
from prediction_model import preprocessing as pp
import pickle as pkl

class LogisticRegressionClassifier():
    """Defines a logistic regression classifier"""

    def __init__(self):
        """Constructs a pipeline for logistic regression classifier"""
        
        pass

    def fit(self, X, y):
        """Fit the pipeline to the data"""
        
        pass
    
    def predict(self, X, prob=False):
        """Predict tthe new seen data"""
        
        pass
    
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
        
