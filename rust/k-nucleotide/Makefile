compile:
	${COMPILER}  -C opt-level=3 -C target-cpu=core2 -C lto -L /usr/local/src/rust-libs knucleotide.rs -o knucleotide.rust-4.rust_run

run:
	./knucleotide.rust-4.rust_run 0 < /root/data/knucleotide-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./knucleotide.rust-4.rust_run 0 < /root/data/knucleotide-input25000000.txt

