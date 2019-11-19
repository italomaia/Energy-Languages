cmpile:
	cp mandelbrot.python3-7.python3 mandelbrot.python3-7.py
measure:
	sudo modprobe msr
	sudo /opt/rapl/main "${BINARY} -OO mandelbrot.python3-7.py 16000" Python mandelbrot

run:
	${BINARY} -OO mandelbrot.python3-7.py 16000

mem:
	/usr/bin/time -v ${BINARY} -OO mandelbrot.python3-7.py 16000
