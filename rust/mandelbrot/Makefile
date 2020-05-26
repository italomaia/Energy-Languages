compile:
	${COMPILER}  -C opt-level=3 -C target-cpu=core2 -C lto -L /usr/local/src/rust-libs mandelbrot.rs -o mandelbrot.rust-4.rust_run

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./mandelbrot.rust-4.rust_run 16000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./mandelbrot.rust-4.rust_run 16000

