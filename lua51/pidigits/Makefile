compile:
	echo "lua51: nothing to do"

run:
	${BINARY} pidigits.lua-5.lua 10000 >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} pidigits.lua-5.lua 10000
