compile:
	echo "lua53: nothing to do"

run:
	${BINARY} nbody.lua-2.lua 50000000 >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -v  ${BINARY} nbody.lua-2.lua 50000000 >> /opt/measures/${TLANG}.txt
