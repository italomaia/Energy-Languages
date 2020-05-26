compile:
	${COMPILER}  -C opt-level=3 -C target-cpu=core2 -C lto  pidigits.rs -o pidigits.rust-2.rust_run

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./pidigits.rust-2.rust_run 10000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./pidigits.rust-2.rust_run 10000

