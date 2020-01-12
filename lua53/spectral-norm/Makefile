compile:
	echo "lua53: nothing to do"

run:
	${BINARY} spectralnorm.lua 5500 >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} spectralnorm.lua 5500
