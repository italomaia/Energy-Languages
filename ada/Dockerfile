FROM energy/base:1

ENV TLANG=ada

COPY . .
RUN apk add gcc-gnat libc-dev gmp-dev apr-util
RUN chown -R 1000:1000 /root && chown -R 1000:1000 /opt
