BINARY=/usr/bin/ravi

compile:

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} spectralnorm.lua 5500

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} spectralnorm.lua 5500

