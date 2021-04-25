compile:
	${BINARY} -O -m compileall .

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} -OO knucleotide.py 0 < /root/data/knucleotide-input25000000.txt > /opt/results/${TLANG}/${TEST_NAME}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -OO knucleotide.py 0 < /root/data/knucleotide-input25000000.txt
