FROM energy/rapl:1

ENV BINARY=/usr/bin/erl
ENV COMPILER=/usr/bin/erlc
COPY . .
RUN apk add erlang
RUN /usr/bin/python3 compile_all.py compile
