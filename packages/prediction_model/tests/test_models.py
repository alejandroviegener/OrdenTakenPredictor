
import pytest
from prediction_model import models
from prediction_model import config
from prediction_model import utils
import numpy as np

TMP_DIR = config.TESTS_DIR / "tmp"

def test_logistic_regression_model_expected_performance():
    """Test model expected performace"""

    # With a logistic regression model and the dataset
    X_train, X_test, y_train, y_test = utils.OrdersDataloader().get_train_test_split(config.TEST_SIZE)
    model = models.LogisticRegressionClassifier()

    # When the model is fitted over the train set
    model.fit(X_train, y_train)

    # Check expected model performace over train and test set
    performance_train = model.performance_summary(X_train, y_train)
    performance_test = model.performance_summary(X_test, y_test)
    assert np.isclose( performance_train["roc_auc"], 0.59833, atol=0.001)
    assert np.isclose( performance_test["roc_auc"], 0.59345, atol=0.001)

def test_random_forest_model_expected_performance():
    """Test model expected performace"""

    # With a logistic regression model and the dataset
    X_train, X_test, y_train, y_test = utils.OrdersDataloader().get_train_test_split(config.TEST_SIZE)
    model = models.RandomForestClassifier()

    # When the model is fitted over the train set
    model.fit(X_train, y_train)

    # Check expected model performace over train and test set
    performance_train = model.performance_summary(X_train, y_train)
    performance_test = model.performance_summary(X_test, y_test)
    assert np.isclose( performance_train["roc_auc"], 0.7081523, atol=0.001)
    assert np.isclose( performance_test["roc_auc"], 0.663338, atol=0.001)

def test_logistic_regression_model_serialization():
    """Test model serialization and deserialization"""

    # With a logistic regression model and the dataset
    X_train, X_test, y_train, y_test = utils.OrdersDataloader().get_train_test_split(config.TEST_SIZE)
    model = models.LogisticRegressionClassifier()

    # When the model is fitted over the train set, serialized and deserialized
    model.fit(X_train, y_train)
    model.save(TMP_DIR / "out.pkl")

    deserialized_model = models.LogisticRegressionClassifier.load(TMP_DIR / "out.pkl")

    # Check expected model performace over train and test set
    performance_train = deserialized_model.performance_summary(X_train, y_train)
    performance_test = deserialized_model.performance_summary(X_test, y_test)
    assert np.isclose( performance_train["roc_auc"], 0.59833, atol=0.001)
    assert np.isclose( performance_test["roc_auc"], 0.59345, atol=0.001)

def test_random_forest_model_serialization():
    """Test model serialization and deserialization"""

    # With a logistic regression model and the dataset
    X_train, X_test, y_train, y_test = utils.OrdersDataloader().get_train_test_split(config.TEST_SIZE)
    model = models.RandomForestClassifier()

    # When the model is fitted over the train set, serialized and deserialized
    model.fit(X_train, y_train)
    model.save(TMP_DIR / "out.pkl")

    deserialized_model = models.RandomForestClassifier.load(TMP_DIR / "out.pkl")

    # Check expected model performace over train and test set
    performance_train = deserialized_model.performance_summary(X_train, y_train)
    performance_test = deserialized_model.performance_summary(X_test, y_test)
    assert np.isclose( performance_train["roc_auc"], 0.7081523, atol=0.001)
    assert np.isclose( performance_test["roc_auc"], 0.663338, atol=0.001)
