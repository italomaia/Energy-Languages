compile:
	echo "luajit: nothing to do"

run:
	${BINARY} pidigits.lua-5.lua 10000 >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -v ${BINARY} pidigits.lua-5.lua 10000 >> /opt/measures/${TLANG}.txt
