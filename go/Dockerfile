FROM energy/base:1

ENV COMPILER=/root/go/bin/go

RUN apk add curl
RUN curl -o go.tar.gz https://dl.google.com/go/go1.14.3.linux-amd64.tar.gz \
    && tar -xvf go.tar.gz
