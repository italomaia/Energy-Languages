compile:
	echo "lua53: nothing to do"

run:
	${BINARY} fannkuchredux.lua 12 > /opt/results/${TEST_NAME}.${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} fannkuchredux.lua 12
