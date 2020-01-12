cmpile:
	echo "python2: nothing to compile"

run:
	${BINARY} -OO mandelbrot.python3-7.py 16000 >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -v ${BINARY} -OO mandelbrot.python3-7.py 16000 >> /opt/measures/${TLANG}.txt
