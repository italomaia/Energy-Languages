compile: ;

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} -OO spectralnorm.py 5500 > /opt/results/${TLANG}/${TEST_NAME}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}/${TEST_NAME}.txt -v ${BINARY} -OO spectralnorm.py 5500
