FROM energy/rapl:1

ENV COMPILER=/usr/bin/rustc
COPY . .
RUN apk add rust
RUN /usr/bin/python3 compile_all.py compile
