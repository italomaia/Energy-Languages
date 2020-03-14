cmpile:
	echo "nothing to do"

run:
	${BINARY} -OO mandelbrot.py 16000 >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -OO mandelbrot.py 16000
