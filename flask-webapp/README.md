# URL shortener Flask Web App

URL-shortener is a project to build a URL shortener that can handle large loads while also demonstrating a knowledge of full stack development.

## Requirements

Install:

* Python3
* Pip

## Build

### Setup Python virtual environment

1. In repository run,`python3 -m venv flaskEnv`
2. Activate virtual environment, `source ./flaskEnv/bin/activate`
3. Install required package, `pip install -r requirements.txt`

## Running

### Development

1. Start MongoDB Server, `docker run -it --rm -p 27017:27017 mongo`
2. Start Flask App, `python app.py`

### Production

Running Flask in production requires Gunicorn.  The full stack would also include reverse proxy Nginx, but details on launching that are in
the root README.  For launching this web app with Gunicorn.

1. Start MongoDB Server, `docker run -it --rm -p 27017:27017 mongo`
2. Start Flask App with gunicorn, `gunicorn --bind 127.0.0.1:8000 --daemon --workers 1 --timeout 600 app:app`

### Container

TODO: This won't work cause the web app will not find the database at localhost:27017, so this will need to be fixed.

1. Build image, `docker build -t flask-webapp .`
2. Start MongoDB Server, `docker run -it --rm -p 27017:27017 mongo`
3. Start web app, `docker run -it --rm -p 5000:5000 flask-webapp`

## Testing

### Linting

Python linting uses pylint and flake8.

A general pylint check will use following pylint command

```bash
source flaskEnv/bin/activate; \
pylint $(git ls-files '*.py');
```

A general flake8 check will check for everything.  But for continuous integration the command used will be `flake8 . --count --show-source --statistics --exclude flaskEnv/`

```bash
source flaskEnv/bin/activate; \
flake8 --exclude flaskEnv/
```

### Integration & Unit Testing

Testing is done using unittest, to start testing, follow the steps

1. Start MongoDB Server, `docker run -it --rm -p 27017:27017 mongo`
2. Start Flask App, `python -m unittest -b`

### Bench marking

Bench marking is contained in directory ./tests/benchmarking.

*apacheBenchmark.sh* is a script using Apache benchmark to send multiple requests concurrently to the web server.
