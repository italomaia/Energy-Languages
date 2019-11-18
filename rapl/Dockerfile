FROM alpine:3

WORKDIR /root
COPY ./code /opt/rapl
COPY ./run.sh /root
RUN apk add kmod make python3

CMD ["sh", "run.sh"]
