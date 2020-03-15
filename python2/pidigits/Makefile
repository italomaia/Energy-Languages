compile:
	echo "python2: nothing to compile"

run:
	${BINARY} -OO pidigits.py 10000 > /opt/results/${TEST_NAME}.${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -OO pidigits.py 10000
