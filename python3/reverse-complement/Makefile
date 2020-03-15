compile:
	echo "nothing to do"

run:
	${BINARY} -OO revcomp.py 0 < /root/data/revcomp-input25000000.txt > /opt/results/${TEST_NAME}.${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -OO revcomp.py 0 < /root/data/revcomp-input25000000.txt

