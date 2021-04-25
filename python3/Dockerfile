FROM energy/base:1

ENV BINARY=/usr/bin/python3
ENV TLANG=python3

COPY . .
RUN apk add gmp-dev mpc1-dev mpfr-dev musl-dev gcc python3-dev py3-pip && /usr/bin/pip3 install gmpy2
RUN chown -R 1000:1000 /root && chown -R 1000:1000 /opt
