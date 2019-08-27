FROM alpine:3

WORKDIR /root
COPY ./code /opt/rapl
COPY ./run.sh /root
RUN apk add kmod make

CMD ["sh", "run.sh"]
