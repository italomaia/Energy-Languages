FROM energy/rapl:1

WORKDIR /root
COPY . /root
RUN apk add lua5.3 && ln -s /usr/bin/lua5.3 /usr/bin/lua
