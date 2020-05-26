compile:
	echo "luajit: nothing to do"

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} binarytrees.lua-2.lua 21 > /opt/results/${TEST_NAME}.${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} binarytrees.lua-2.lua 21
