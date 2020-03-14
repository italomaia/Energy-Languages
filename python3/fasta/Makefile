compile:
	echo "nothing to do"

run:
	${BINARY} -OO fasta.py 25000000 >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -OO fasta.py 25000000
