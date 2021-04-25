compile:
	${BINARY} -O -m compileall -l .

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} regexredux.py 0 < /root/data/regexredux-input5000000.txt > /opt/results/${TLANG}/${TEST_NAME}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}/${TEST_NAME}.txt -v ${BINARY} regexredux.py 0 < /root/data/regexredux-input5000000.txt
