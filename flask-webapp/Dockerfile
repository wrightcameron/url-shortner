FROM python:3.8.10

ENV APPDIR /usr/src/app

RUN mkdir -p $APPDIR; \
    adduser flask; \
    chown flask:flask $APPDIR; \
    echo "export PATH=$PATH:/home/flask/.local/bin/" >> /home/flask/.bashrc;


USER flask
WORKDIR $APPDIR

#COPY requirements.txt /usr/src/app
COPY . .
RUN pip install -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "1", "--timeout", "600", "app:app"]
