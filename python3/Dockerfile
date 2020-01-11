FROM energy/base:1

ENV BINARY=/usr/bin/python3
COPY . .
RUN apk add python3
RUN /usr/bin/python3 compile_all.py compile
