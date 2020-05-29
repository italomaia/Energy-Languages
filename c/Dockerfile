FROM energy/base:1

ENV BINARY=/usr/bin/gcc
COPY . .
RUN apk add gcc musl-dev apr-dev 
RUN /usr/bin/python3 compile_all.py compile
