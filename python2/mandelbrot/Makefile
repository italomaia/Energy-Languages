cmpile:
	echo "python2: nothing to compile"

run:
	${BINARY} -OO mandelbrot.py 16000 > /opt/results/${TEST_NAME}.${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -OO mandelbrot.py 16000
