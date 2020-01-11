FROM energy/base:1

ENV BINARY=/usr/bin/perl
COPY . .
RUN apk add perl
RUN /usr/bin/python3 compile_all.py compile
