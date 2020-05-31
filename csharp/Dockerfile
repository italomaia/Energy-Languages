FROM energy/base:1

ENV BINARY=/usr/bin/mono
COPY . .
RUN apk add -X http://dl-cdn.alpinelinux.org/alpine/edge/testing mono gmp-dev
RUN /usr/bin/python3 compile_all.py compile
