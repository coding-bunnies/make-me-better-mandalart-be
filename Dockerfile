FROM python:3.12.2-slim

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /
RUN chmod +x /wait-for-it.sh

RUN apt-get update && apt-get upgrade -y
RUN apt-get install gcc default-libmysqlclient-dev pkg-config -y

WORKDIR /make-me-better-mandalart-be
COPY . /make-me-better-mandalart-be
RUN pip install -r requirements.txt

