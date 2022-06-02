FROM python:3.8.10

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

#COPY requirements.txt /usr/src/app
COPY . .
RUN pip install -r requirements.txt

# TODO Change user so to not run as root
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "1", "--timeout", "600", "app:app"]
