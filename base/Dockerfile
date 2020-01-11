FROM alpine:3.10

ENV TIME="cmd:%C;real %es;user %Us ;sys  %Ss ;memory:%MKB ;cpu %P"

WORKDIR /root
COPY ./compile_all.py .
RUN apk --no-cache add make python3

