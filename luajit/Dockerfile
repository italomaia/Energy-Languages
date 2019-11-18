FROM energy/rapl:1

WORKDIR /root
COPY . /root
RUN apk add luajit && ln -s /usr/bin/luajit /usr/bin/lua
