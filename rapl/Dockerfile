FROM alpine:3

WORKDIR /root
COPY ./code /opt/rapl
COPY ./run.sh .
COPY ./compile_all.py .
COPY knucleotide-input25000000.txt .
COPY revcomp-input25000000.txt .
COPY regexredux-input5000000.txt .

RUN apk add kmod make python3

CMD ["sh", "run.sh"]
