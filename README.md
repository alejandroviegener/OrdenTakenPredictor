# Order Taken Predictor

System that exposes a classification model in an API, to predict if a courier will take an optional order


# Table of Contents
1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Tests](#tests)
5. [Application Design Basics](#design)

## Requirements  <a name="requirements"></a>

This application requieres the following for its installation and usage:

* [git][git] 
* [Docker][docker]


[git]: https://git-scm.com/
[docker]: https://www.docker.com/   

## Installation <a name="installation"></a>

Download the source repository to the desired location: 

```bash
git clone git@github.com:alejandroviegener/OrdenTakenPredictor.git
```

From now on this directory will be refered to as $REPO_BASE_DIR.

The application is dockerized, to build the Docker image follow these steps:

1) Change to the repo base directory:

```bash
cd $REPO_BASE_DIR
```

2) Build the docker images:

```bash
docker-compose build
```

The script will create two docker images. To confirm the creation of the images, execute:

```bash
docker image ls
```

A docker image named mongo and another named rappi-prediction-api must be listed.

## Usage <a name="usage"></a>

1) Go to the repo base directory:

```bash
cd $REPO_BASE_DIR
```

2) Start the system:

```bash
docker-compose up
```

Or alternaively run in detached mode:

```bash
docker-compose up -d
```

3) See the API documentation:

Open your browser and go to the url http://127.0.0.1:8000/docs#/

Two endpoints where implemented:

- version: gets the version of the system
- prediction: requests prediction given the input features


## Tests <a name="tests"></a>

To run the system tests:

1) Start the system as explained previously
2) Execute the following command in a new terminal window: 

```bash
docker exec -it rapi-prediction-api ./test.sh
```

## Application Design Basics <a name="design"></a>

Three python packages where implemented:

1) **mongo_db**: defines a simple client class for connection to the server and document insertion.
2) **predicion_api**: implementes the API of the system, **FastAPI** was used
3) **prediction_model**: Predicton model implemented as a sklearn pipeline. 

The system was dockerized in two containers:

1) One that contains the prediction model and the API, and
2) the databse container

