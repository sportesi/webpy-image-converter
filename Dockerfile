FROM python:3.7-alpine

RUN apk update && apk add \
    musl-dev \
    linux-headers \
    jpeg-dev \
    gcc \
    python3-dev \
    libjpeg-turbo-dev \
    zlib-dev

RUN pip install virtualenv