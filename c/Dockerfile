FROM energy/base:1

ENV BINARY=/usr/bin/gcc
ENV TLANG=c
COPY . .
RUN apk add gcc musl-dev apr-dev gmp-dev pcre-dev
RUN chown -R 1000:1000 /root && chown -R 1000:1000 /opt
