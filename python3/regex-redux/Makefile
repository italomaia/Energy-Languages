compile:
	${BINARY} -O -m compileall .

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} -OO regexredux.py 0 < /root/data/regexredux-input5000000.txt > /opt/results/${TLANG}/${TEST_NAME}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -OO regexredux.py 0 < /root/data/regexredux-input5000000.txt
