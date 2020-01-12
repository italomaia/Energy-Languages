compile:
	echo "python2: nothing to compile"

run:
	${BINARY} -OO fasta.python3-3.py 25000000 >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -v  ${BINARY} -OO fasta.python3-3.py 25000000 >> /opt/measures/${TLANG}.txt
