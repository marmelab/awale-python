FROM python:3

RUN mkdir /src
WORKDIR /src
ADD . /src/
