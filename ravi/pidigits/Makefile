BINARY=/usr/bin/ravi

compile:

xprepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} pidigits.lua-5.lua 10000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} pidigits.lua-5.lua 10000



