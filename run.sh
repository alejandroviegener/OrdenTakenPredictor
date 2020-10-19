#!/bin/bash

cd ./packages/prediction_api/prediction_api
uvicorn main:app --reload