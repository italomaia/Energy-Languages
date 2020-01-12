compile:
	echo "luajit: nothing to do"

run:
	${BINARY} binarytrees.lua-2.lua 21 >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -v ${BINARY} binarytrees.lua-2.lua 21 >> /opt/measures/${TLANG}.txt
