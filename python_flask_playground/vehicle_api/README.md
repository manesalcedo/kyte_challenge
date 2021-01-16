# Python Flask Playground

## Local Flask Development Environment

### Install OS Prerequisites

- Python 3.9
- Virtualenv

#### On Ubuntu

```
$ sudo apt-get update
$ sudo apt-get install -y python python-pip python-virtualenv
```

#### On Mac (with brew)
```
$ brew install python python-pip python-virtualenv

```

### Install and run app

Create and activate a virtualenv
```
$ python3.9 -m venv venv  
$ source venv/bin/activate
```

Install the requirements
```
$ pip3 install -r requirements.txt
$ pip3 install -e .
```

Setup the following environment variable
```
$ export FLASK_APP=vehicle_api
```

Start the API!

```
$ flask run
```

Check health status (on port 5000)
```
$ curl http://127.0.0.1:5000/api/health

```
Try the api
```
$ curl http://127.0.0.1:5000/api/vehicles?sort=model&status=available&model=Versa&page=2&per_page=1
```

## Local Web Server (nginx-uWSGI) Test Development Environment on Mac OS

### Install OS Prerequisites

- Python 3.9
- Virtualenv
- nginx

```
$ brew install python python-pip python-virtualenv nginx

```

### Install and run app

Create and activate a virtualenv
```
$ python3.9 -m venv venv  
$ source venv/bin/activate
```

Install the requirements
```
$ pip install -r requirements.txt
$ pip install -e .
```

Start uWSGI

```
$  uwsgi ./wsgi_local.ini
```

Configure nginx
```
$ vi /usr/local/etc/nginx/nginx.conf
```
Add the following lines:
```
    server {
        listen 80;
        server_name localhost;
        location / {
            include uwsgi_params;
            uwsgi_pass unix:/path/to/vehicle_api/main.sock;
        }
    }
```

Start nginx
```
$ sudo brew services start nginx
```

Check health status (on port 8080)
```
$ curl http://127.0.0.1:8080/api/health

```
Try the api
```
$ curl 'http://127.0.0.1:8080/api/vehicles?sort=model&status=available&model=Versa&page=2&per_page=1'
```
