compile:
	${COMPILER}  -C opt-level=3 -C target-cpu=core2 -C lto -L /usr/local/src/rust-libs revcomp.rs -o revcomp.rust-2.rust_run

run:
	./revcomp.rust-2.rust_run 0 < /root/data/revcomp-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./revcomp.rust-2.rust_run 0 < /root/data/revcomp-input25000000.txt

