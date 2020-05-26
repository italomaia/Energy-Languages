BINARY=/usr/bin/ravi

compile:

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} mandelbrot.lua-6.lua 16000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ${BINARY} mandelbrot.lua-6.lua 16000

