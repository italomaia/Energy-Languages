compile:
	${COMPILER}  -C opt-level=3 -C target-cpu=core2 -C lto -L /usr/local/src/rust-libs mandelbrot.rs -o mandelbrot.rust-4.rust_run

measure:
	/opt/rapl/main "./mandelbrot.rust-4.rust_run 16000" Rust mandelbrot

run:
	./mandelbrot.rust-4.rust_run 16000

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./mandelbrot.rust-4.rust_run 16000

valgrind:
	valgrind --tool=massif --stacks=yes  ./mandelbrot.rust-4.rust_run 16000
