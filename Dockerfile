FROM alpine:latest
WORKDIR /code
RUN apk add --no-cache --virtual .build-deps \
    build-base libffi-dev openssl-dev libxslt-dev && \
    apk add --no-cache git python3-dev && \
    echo -e "requests\ngooglemaps\nscrapy" > requirements.txt && \
    pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt && \
    apk del .build-deps && \
    git clone https://github.com/tomkeegan/restaurant-menus.git 