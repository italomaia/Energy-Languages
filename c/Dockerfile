FROM energy/rapl:1

ENV BINARY=/usr/bin/gcc
COPY . .
RUN apk add gcc
RUN /usr/bin/python3 compile_all.py compile
