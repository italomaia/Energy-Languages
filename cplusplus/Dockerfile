FROM energy/base:1

ENV BINARY=/usr/bin/g++
COPY . .
RUN apk add g++ musl-dev apr-dev gmp-dev pcre-dev
RUN /usr/bin/python3 compile_all.py compile
