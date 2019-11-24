compile:

measure:
	sudo /opt/rapl/main "${BINARY} mandelbrot.perl 16000" Perl mandelbrot

run:
	${BINARY} mandelbrot.perl 16000

mem:
	/usr/bin/time -v ${BINARY} mandelbrot.perl 16000

valgrind:
	valgrind --tool=massif --stacks=yes ${BINARY} mandelbrot.perl 16000
