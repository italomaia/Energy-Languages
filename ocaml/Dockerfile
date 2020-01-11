FROM energy/base:1

ENV COMPILER=/usr/bin/ocamlopt
COPY . .
RUN apk add ocaml
RUN /usr/bin/python3 compile_all.py compile
