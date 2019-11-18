FROM alpine:latest
WORKDIR /code
COPY pip3.txt ./
RUN apk add --no-cache --virtual .build-deps \
    build-base libffi-dev openssl-dev \
    libxslt-dev python3-dev && \
    pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r pip3.txt && \
    apk del .build-deps
COPY . .