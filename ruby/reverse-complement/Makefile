compile:


prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} -W0 revcomp.yarv-3.yarv 0 < /root/data/revcomp-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -W0 revcomp.yarv-3.yarv 0 < /root/data/revcomp-input25000000.txt

