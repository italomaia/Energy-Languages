BINARY=/usr/bin/ravi

compile:

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} fannkuchredux.lua 12

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} fannkuchredux.lua 12

