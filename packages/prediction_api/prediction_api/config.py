"""Some global configurations for the prediction api package"""

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

