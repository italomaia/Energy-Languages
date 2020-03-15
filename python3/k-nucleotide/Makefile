compile:
	echo "nothing to do"

run:
	${BINARY} -OO knucleotide.py 0 < /root/data/knucleotide-input25000000.txt > /opt/results/${TEST_NAME}.${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -OO knucleotide.py 0 < /root/data/knucleotide-input25000000.txt
