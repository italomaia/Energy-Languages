FROM energy/base:1

ENV BINARY=/usr/bin/luajit
ENV TLANG=luajit

COPY . .
RUN apk add luajit
RUN /usr/bin/python3 compile_all.py compile
