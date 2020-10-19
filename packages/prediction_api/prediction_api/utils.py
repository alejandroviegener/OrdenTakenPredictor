"""Utility functions"""

from input_output_models import Features
from typing import List
import pandas as pd


def features_list_to_dataframe(features_list: List[Features]):
    """Create a pandas dataframe from an input features list"""

    if len(features_list) == 0:
        return None

    # Get the keys of the freatures
    keys = features_list[0].to_dict().keys()

    # Create a dictionary with those keys and a list for each
    features_dict = { key: [] for key in keys} 
    
    # Fill the lists
    for features in features_list:
        for key, value in features.to_dict().items():
            features_dict[key].append(value)
    
    # Create dataframe with resulting features dict
    X = pd.DataFrame(features_dict)
    return X