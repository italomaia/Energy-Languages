compile:
	${COMPILER}  -C opt-level=3 -C target-cpu=core2 -C lto -L /usr/local/src/rust-libs regexredux.rs -o regexredux.rust_run

run:
	./regexredux.rust_run 0 < /root/data/regexredux-input5000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./regexredux.rust_run 0 < /root/data/regexredux-input5000000.txt

