compile:
	echo "python2: nothing to compile"

run:
	${BINARY} -OO fasta.py 25000000 > /opt/results/${TEST_NAME}.${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ${BINARY} -OO fasta.py 25000000
