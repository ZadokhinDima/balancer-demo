FROM openresty/openresty:alpine-fat

RUN apk add --no-cache --virtual .build-deps \
    gcc \
    libc-dev \
    make \
    openssl-dev \
    pcre-dev \
    zlib-dev \
    linux-headers \
    curl \
    geoip-dev \
    alpine-sdk \
    findutils \
    libmaxminddb-dev \
    git \
    perl \
    luarocks \
    && luarocks install mmdblua