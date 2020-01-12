compile:
	${COMPILER}  -C opt-level=3 -C target-cpu=core2 -C lto -L /usr/local/src/rust-libs binarytrees.rs -o binarytrees.rust-2.rust_run

run:
	./binarytrees.rust-2.rust_run 21

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./binarytrees.rust-2.rust_run 21

