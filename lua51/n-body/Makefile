compile:
	echo "lua51: nothing to do"

run:
	${BINARY} nbody.lua-2.lua 50000000 > /opt/results/${TEST_NAME}.${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ${BINARY} nbody.lua-2.lua 50000000
