compile:
	cp fasta.python3-3.python3 fasta.python3-3.py

run:
	${BINARY} -OO fasta.python3-3.py 25000000 >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -OO fasta.python3-3.py 25000000
