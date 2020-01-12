compile:
	${COMPILER}  -C opt-level=3 -C target-cpu=core2 -C lto -L /usr/local/src/rust-libs spectralnorm.rs -o spectralnorm.rust-4.rust_run

run:
	./spectralnorm.rust-4.rust_run 5500

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./spectralnorm.rust-4.rust_run 5500

