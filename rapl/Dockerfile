FROM alpine:3.10

WORKDIR /root
COPY ./code /opt/rapl
COPY ./compile_all.py .

RUN apk --no-cache add make python3

RUN apk --no-cache --virtual build-dependencies add \
    kmod \
    gcc \
    libc-dev \
    # installs modify system registers module
    # TODO command below is broken
    && modprobe msr \
    # compiles rapl
    && cd /opt/rapl \
    && make main \
    # clean-up S2
    && apk del build-dependencies

CMD ["sh", "run.sh"]
