FROM energy/base:1

ENV BINARY=/usr/bin/lua5.3
COPY . .
RUN apk add lua5.3
RUN /usr/bin/python3 compile_all.py compile
