compile:
	echo "nothing to do"

run:
	${BINARY} -OO regexredux.py 0 < /root/data/regexredux-input5000000.txt > /opt/results/${TEST_NAME}.${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -OO regexredux.py 0 < /root/data/regexredux-input5000000.txt
