
import pytest 
from prediction_model import config
from prediction_model import utils

def test_orders_dataloader():
    """Check that the data is loaded correctly"""

    # Given the dataset loaded
    X_train, X_test, y_train, y_test = utils.OrdersDataloader().get_train_test_split(0.25)
    
    # Then check the correct size returned
    assert X_train.shape == (110230, 6)
    assert X_test.shape == (36744, 6)
    assert y_train.shape == (110230,)
    assert y_test.shape == (36744,)


