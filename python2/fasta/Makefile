compile: ;

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} -OO fasta.py 25000000 > /opt/results/${TLANG}/${TEST_NAME}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}/${TEST_NAME}.txt -v  ${BINARY} -OO fasta.py 25000000
