# From image
FROM python:3.8-slim

# Set working dir on image
WORKDIR /opt/app

# Copy prediction model and api
COPY ./packages . 
COPY start_api.sh start_api.py requirements.txt ./

# Install python packages
RUN pip install -e prediction_model && \
    pip install -e prediction_api && \
    pip install -e mongo_db && \
    pip install -r requirements.txt 

# Used port in API
EXPOSE 8000

# Start API
CMD ["./start_api.sh"]
