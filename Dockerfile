FROM alpine:latest
WORKDIR /code
COPY ./config.py ./config.py
RUN apk add --no-cache \
    build-base libffi-dev openssl-dev libxslt \ 
    libxslt-dev git python3-dev && \
    echo -e "requests\ngooglemaps\nscrapy" > requirements.txt && \
    pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt && \
    git config --global user.email "tomkeegan835@gmail.com" && \
    git config --global user.name "Tom Keegan" && \
    git config --global url.'https://876439f1bf03a2e443433f2c819c7bb51cd87f0a:x-oauth-basic@github.com/'.inst