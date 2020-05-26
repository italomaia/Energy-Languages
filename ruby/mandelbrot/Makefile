compile:


prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} -W0 mandelbrot.yarv-5.yarv 16000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -W0 mandelbrot.yarv-5.yarv 16000

