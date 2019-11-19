compile:
	cp mandelbrot.hipe-2.hipe mandelbrot.erl
	${COMPILER} +native +"{hipe, [o3]}" mandelbrot.erl
measure:
	sudo modprobe msr
	sudo /opt/rapl/main "${BINARY} -smp enable -noshell -run  mandelbrot main 16000" Erlang mandelbrot

run:
	${BINARY} -smp enable -noshell -run  mandelbrot main 16000

mem:
	/usr/bin/time -v  ${BINARY} -smp enable -noshell -run  mandelbrot main 16000

valgrind:
	valgrind --tool=massif --stacks=yes  ${BINARY} -smp enable -noshell -run  mandelbrot main 16000
