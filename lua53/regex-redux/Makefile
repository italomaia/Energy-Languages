compile:
	echo "lua53: nothing to do"

run:
	${BINARY} regexredux.lua-2.lua 0 < ../../regexredux-input50000.txt >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -v ${BINARY} regexredux.lua-2.lua 0 < ../../regexredux-input50000.txt >> /opt/measures/${TLANG}.txt
