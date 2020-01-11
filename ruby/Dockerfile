FROM energy/base:1

ENV BINARY=/usr/bin/ruby
COPY . .
RUN apk add ruby
RUN /usr/bin/python3 compile_all.py compile
