compile:
	${COMPILER}  -C opt-level=3 -C target-cpu=core2 -C lto -C llvm-args='-unroll-threshold=500' nbody.rs -o nbody.rust-2.rust_run

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./nbody.rust-2.rust_run 50000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./nbody.rust-2.rust_run 50000000

