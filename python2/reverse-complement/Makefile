compile:
	echo "python2: nothing to compile"

run:
	${BINARY} -OO revcomp.python3-6.py 0 < /root/data/revcomp-input25000000.txt >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -v ${BINARY} -OO revcomp.python3-6.py 0 < /root/data/revcomp-input25000000.txt >> /opt/measures/${TLANG}.txt

