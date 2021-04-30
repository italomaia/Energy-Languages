FROM energy/base:1

ENV BINARY=/usr/bin/g++
ENV TLANG=cplusplus
COPY . .
RUN apk add g++ musl-dev apr-dev gmp-dev pcre-dev boost-dev
RUN chown -R 1000:1000 /root && chown -R 1000:1000 /opt
