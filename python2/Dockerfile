FROM energy/base:1

ENV BINARY=/usr/bin/python2
ENV TLANG=python2

COPY . .
RUN apk add python2
RUN chown -R 1000:1000 /root && chown -R 1000:1000 /opt
