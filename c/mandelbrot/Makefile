compile:
	/usr/bin/gcc -pipe -Wall -O3 -fomit-frame-pointer -march=native -mno-fma -fno-finite-math-only -mfpmath=sse -msse2 -fopenmp mandelbrot.gcc-6.c -o mandelbrot.gcc-6.gcc_run

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./mandelbrot.gcc-6.gcc_run 16000 > /opt/results/${TLANG}/${TEST_NAME}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./mandelbrot.gcc-6.gcc_run 16000
