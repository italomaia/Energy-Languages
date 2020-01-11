FROM energy/base:1

ENV BINARY=/usr/bin/python2
COPY . .
RUN apk add python2
RUN /usr/bin/python3 compile_all.py compile
