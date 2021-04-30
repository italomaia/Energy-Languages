compile:
	/usr/bin/gcc -pipe -Wall -O3 -fomit-frame-pointer -march=native -mfpmath=sse -msse3 nbody.gcc-4.c -o nbody.gcc-4.gcc_run -lm

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./nbody.gcc-4.gcc_run 50000000 > /opt/results/${TLANG}/${TEST_NAME}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./nbody.gcc-4.gcc_run 50000000
