compile:


prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} -W0 fasta.yarv-3.yarv 25000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ${BINARY} -W0 fasta.yarv-3.yarv 25000000

