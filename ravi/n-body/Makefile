BINARY=/usr/bin/ravi

compile:

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} nbody.lua-2.lua 50000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ${BINARY} nbody.lua-2.lua 50000000

