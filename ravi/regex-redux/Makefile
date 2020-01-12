BINARY=/usr/bin/ravi

compile:

xrun:
	${BINARY} regexredux.lua-2.lua 0 < ../../regexredux-input50000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} regexredux.lua-2.lua 0 < ../../regexredux-input50000.txt

