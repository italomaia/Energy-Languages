compile:
	echo "lua51: nothing to do"

run:
	${BINARY} regexredux.lua-2.lua 0 < ../../regexredux-input50000.txt > /opt/results/${TEST_NAME}.${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} regexredux.lua-2.lua 0 < ../../regexredux-input50000.txt
