compile:
	echo "lua53: nothing to do"

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} spectralnorm.lua 5500 > /opt/results/${TEST_NAME}.${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} spectralnorm.lua 5500
