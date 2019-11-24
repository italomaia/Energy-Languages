BINARY=/usr/bin/ravi

compile:

measure:
	/opt/rapl/main "${BINARY}  mandelbrot.lua-6.lua 16000" Lua mandelbrot

run:
	${BINARY}  mandelbrot.lua-6.lua 16000

mem:
	/usr/bin/time -v  ${BINARY}  mandelbrot.lua-6.lua 16000

valgrind:
	valgrind --tool=massif --stacks=yes  ${BINARY}  mandelbrot.lua-6.lua 16000
