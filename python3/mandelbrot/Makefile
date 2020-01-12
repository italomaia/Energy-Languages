cmpile:
	cp mandelbrot.python3-7.python3 mandelbrot.python3-7.py

run:
	${BINARY} -OO mandelbrot.python3-7.py 16000 >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -v ${BINARY} -OO mandelbrot.python3-7.py 16000 >> /opt/measures/${TLANG}.txt
