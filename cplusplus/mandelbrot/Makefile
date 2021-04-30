compile:
	/usr/bin/g++ -c -pipe -O3 -fomit-frame-pointer -march=native -mfpmath=sse -msse2 -mfpmath=sse -msse2 -fopenmp -mno-fma --std=c++14 mandelbrot.gpp-6.c++ -o mandelbrot.gpp-6.c++.o &&  /usr/bin/g++ mandelbrot.gpp-6.c++.o -o mandelbrot.gpp-6.gpp_run -fopenmp

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./mandelbrot.gpp-6.gpp_run 16000 > /opt/results/${TLANG}/${TEST_NAME}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./mandelbrot.gpp-6.gpp_run 16000

