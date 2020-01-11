FROM energy/base:1

ENV BINARY=/usr/bin/lua5.1
COPY . .
RUN apk add lua5.1
RUN /usr/bin/python3 compile_all.py compile
