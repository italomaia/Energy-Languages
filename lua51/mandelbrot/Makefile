compile:
	echo "lua51: nothing to do"

run:
	${BINARY} mandelbrot.lua-6.lua 16000 >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ${BINARY} mandelbrot.lua-6.lua 16000
