"""Global general package configurations"""

import pathlib
import prediction_model

# General
RANDOM_SEED = 314
TEST_SIZE = 0.25

# Directories and files
PACKAGE_ROOT = pathlib.Path(prediction_model.__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"
TRAINED_MODEL_FILE = "model.pkl"
TRAINED_MODEL_FILE_PATH = TRAINED_MODEL_DIR / TRAINED_MODEL_FILE
DATASET_DIR = PACKAGE_ROOT / "datasets"
DATASET_FILE = "orders.csv"
DATASET_FILE_PATH = DATASET_DIR / DATASET_FILE
