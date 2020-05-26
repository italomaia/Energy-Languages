BINARY=/usr/bin/ravi

compile:

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} binarytrees.lua-2.lua 21

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} binarytrees.lua-2.lua 21

