compile:


measure:
	/opt/rapl/main "${BINARY} -W0 mandelbrot.yarv-5.yarv 16000" Ruby mandelbrot

run:
	${BINARY} -W0 mandelbrot.yarv-5.yarv 16000

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -W0 mandelbrot.yarv-5.yarv 16000

valgrind:
	valgrind --tool=massif --stacks=yes ${BINARY} -W0 mandelbrot.yarv-5.yarv 16000
