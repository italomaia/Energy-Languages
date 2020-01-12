compile:
	/usr/bin/gcc -pipe -Wall -O3 -fomit-frame-pointer -march=native -fopenmp -mfpmath=sse -msse2 spectralnorm.gcc-4.c -o spectralnorm.gcc-4.gcc_run -lm
measure:
	/opt/rapl/main "./spectralnorm.gcc-4.gcc_run 5500" C spectral-norm

run:
	./spectralnorm.gcc-4.gcc_run 5500

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./spectralnorm.gcc-4.gcc_run 5500

