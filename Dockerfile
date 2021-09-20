FROM python:3.7-alpine

RUN apk update && apk add \
    musl-dev \
    libpng-dev \
    jpeg-dev \
    gcc \
    zlib-dev \
    libwebp-dev

RUN pip install virtualenv