cmpile:
	echo "python2: nothing to compile"

measure:
	modprobe msr
	/opt/rapl/main "${BINARY} -OO mandelbrot.python3-7.py 16000" /opt/result/python2 mandelbrot

run:
	${BINARY} -OO mandelbrot.python3-7.py 16000

mem:
	/usr/bin/time -v ${BINARY} -OO mandelbrot.python3-7.py 16000
