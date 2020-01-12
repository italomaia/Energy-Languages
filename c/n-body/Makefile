compile:
	/usr/bin/gcc -pipe -Wall -O3 -fomit-frame-pointer -march=native -mfpmath=sse -msse3 nbody.gcc-4.c -o nbody.gcc-4.gcc_run -lm
run:
	./nbody.gcc-4.gcc_run 50000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./nbody.gcc-4.gcc_run 50000000
