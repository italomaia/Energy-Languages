compile:
	echo "lua53: nothing to do"

run:
	${BINARY} binarytrees.lua-2.lua 21 >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} binarytrees.lua-2.lua 21
