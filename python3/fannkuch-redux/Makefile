compile:
	echo "nothing to do"

run:
	${BINARY} -OO fannkuchredux.py 12 > /opt/results/${TEST_NAME}.${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -OO fannkuchredux.py 12
