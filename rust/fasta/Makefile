compile:
	${COMPILER}  -C opt-level=3 -C target-cpu=core2 -C lto -L /usr/local/src/rust-libs fasta.rs -o fasta.rust-2.rust_run

run:
	./fasta.rust-2.rust_run 25000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./fasta.rust-2.rust_run 25000000

