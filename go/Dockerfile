FROM energy/base:1

ENV COMPILER=/usr/bin/go

COPY . .

RUN apk add --no-cache musl-dev gmp-dev pcre-dev git go
RUN go get github.com/glenn-brown/golang-pkg-pcre/src/pkg/pcre
