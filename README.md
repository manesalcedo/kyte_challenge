# Python/Flask API Playground 
# Vehicle API


## Local Deployment
To run it locally (i.e. without docker) please check the following instructions.

### Prerequisites
- python 3.9

### Backend Installation

1. Create and activate a virtualenv
```
$ python3.9 -m venv venv  
$ source venv/bin/activate
```

2. Install the requirements
```
$ pip3 install -r requirements.txt
$ pip3 install -e .
```

3. Setup the following environment variable
```
$ export FLASK_APP=vehicle_api
```

### Start the Flask app

1. To start the flask app, under the directory `./python_flask_playground/vehicle-api`, execute:
```
$ flask run
```
2. To check the app's health status (on port 5000)
```
$ curl http://127.0.0.1:5000/api/health

```

## Docker Deployment
### Build
1. Specify the image version you would like to build:
e.g.
```
$ export VERSION=latest
```
2. Under the current directory, execute

```
$ docker-compose build
```

### Push each image to ECR
1. Get the credentials (Access Key ID, Secret Access Key, etc.) to push docker images to Amazon Web Services' Elastic Container Repository from anyone with admin access to AWS's website
2. Set up aws configure on your host(only once),
```
$ aws configure --profile py-playground-ecr

    AWS Access Key ID [None]: XXXX
    AWS Secret Access Key [None]: XXXX
    Default region name [None]: ap-northeast-1
    Default output format [None]: json
```
3. Log into ECR
```
$ $(aws ecr get-login --no-include-email --region ap-northeast-1 --profile py-playground-ecr)
```
4. After building the images you want to push, to push the docker image's to ECR:
```
$ docker-compose push
```

### Start the docker containers
under this directory,
```
$ docker-compose up -d
```

### Test the app!

Check health status (on port 8080)
```
$ curl http://127.0.0.1:80/api/health

```
Try the api
```
$ curl 'http://127.0.0.1:80/api/vehicles?sort=model&status=available&model=Versa&page=2&per_page=1'
```
