compile:
	echo "luajit: nothing to do"

run:
	${BINARY} spectralnorm.lua 5500 > /opt/results/${TEST_NAME}.${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} spectralnorm.lua 5500
