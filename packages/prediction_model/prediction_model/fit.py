
from prediction_model import models
from prediction_model import utils
from prediction_model import config

# Globals
TEST_SIZE = config.TEST_SIZE
TRAINED_MODEL_FILE_PATH = config.TRAINED_MODEL_FILE_PATH

def fit_and_save():

    # Get the dataset data 
    data = utils.OrdersDataloader().get_train_test_split(TEST_SIZE)
    X_train, _, y_train, _ = data

    # Fit the model
    model = models.LogisticRegressionClassifier()
    model.fit(X_train, y_train)

    # Save the model
    model.save(TRAINED_MODEL_FILE_PATH)

if __name__ == "__main__":
    fit_and_save()
