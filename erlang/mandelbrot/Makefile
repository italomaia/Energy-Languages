compile:
	cp mandelbrot.hipe-2.hipe mandelbrot.erl
	${COMPILER} +native +"{hipe, [o3]}" mandelbrot.erl
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} -smp enable -noshell -run  mandelbrot main 16000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ${BINARY} -smp enable -noshell -run  mandelbrot main 16000

