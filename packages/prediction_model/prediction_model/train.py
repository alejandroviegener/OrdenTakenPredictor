
from prediction_model import predictor
from prediction_model import config


def fit_and_serialize_model():
    """Comments"""
    # Load data
    data = Dataloader.load(config.DATASET_PATH)

    # Remove outliers

    # Separate in train and test

    # Create model
    model = predictor.OrderTakenPredictor()

    # Fit and serialize model
    model.fit(X_train, test)
    model.save(config.OUTPUT_MODEL_FILE_PATH)

if __name__ == "__main__":
    fit_and_serialize_model()


