compile:
	${BINARY} -O -m compileall -l .

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} knucleotide.py 0 < /root/data/knucleotide-input25000000.txt > /opt/results/${TLANG}/${TEST_NAME}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}/${TEST_NAME}.txt -v ${BINARY} knucleotide.py 0 < /root/data/knucleotide-input25000000.txt
