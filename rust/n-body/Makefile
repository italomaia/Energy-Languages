compile:
	${COMPILER}  -C opt-level=3 -C target-cpu=core2 -C lto -C llvm-args='-unroll-threshold=500' nbody.rs -o nbody.rust-2.rust_run

measure:
	/opt/rapl/main "./nbody.rust-2.rust_run 50000000" Rust n-body

run:
	./nbody.rust-2.rust_run 50000000

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./nbody.rust-2.rust_run 50000000

valgrind:
	valgrind --tool=massif --stacks=yes ./nbody.rust-2.rust_run 50000000
