FROM adminer:latest

USER root

RUN apt-get update && apt-get install -y php-mongodb

USER adminer
