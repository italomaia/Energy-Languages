compile:
	echo "python2: nothing to compile"

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} -OO revcomp.py 0 < /root/data/revcomp-input25000000.txt > /opt/results/${TLANG}/${TEST_NAME}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}/${TEST_NAME}.txt -v ${BINARY} -OO revcomp.py 0 < /root/data/revcomp-input25000000.txt

