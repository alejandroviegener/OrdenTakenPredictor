"""Some global configurations for the prediction api package"""

import prediction_api
import logging
import colorlog

# Define the root logger
LOGGER_NAME = "prediction_api"
logger =  logging.getLogger(LOGGER_NAME)
logger.setLevel(logging.INFO)

# Set logger handler and formatter
stream_handler = logging.StreamHandler()
formatter = colorlog.ColoredFormatter('%(log_color)s%(levelname)s%(reset)s: <%(name)s> %(bold)s%(message)s')
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# Version 
VERSION = "0.1.0"

predictions_persistance_handler = None
"""Handler for predictions persistance

    Should recieve an iterable of dicts and persist the data
    Example:
         
        import prediction_api.config as api_config

         def handler(dictionaries_list):
             for dictionary in dictionaries_list:
                 print("Persisting dictionary in some way")

        api_config.predictions_persistance_handler = handler
"""

