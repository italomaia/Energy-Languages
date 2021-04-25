compile:
	${BINARY} -O -m compileall -l .

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} mandelbrot.py 16000 > /opt/results/${TLANG}/${TEST_NAME}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}/${TEST_NAME}.txt -v ${BINARY} mandelbrot.py 16000
