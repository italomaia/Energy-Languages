compile:
	echo "lua51: nothing to do"

run:
	${BINARY} fannkuchredux.lua 12 >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -v ${BINARY} fannkuchredux.lua 12 >> /opt/measures/${TLANG}.txt
