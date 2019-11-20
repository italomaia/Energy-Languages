FROM alpine:3.10

WORKDIR /root
COPY ./code /opt/rapl
COPY ./compile_all.py .

RUN apk add kmod make python3

CMD ["sh", "run.sh"]
