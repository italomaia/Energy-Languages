compile:
	/usr/bin/gcc -pipe -Wall -O3 -fomit-frame-pointer -march=native -fopenmp -D_FILE_OFFSET_BITS=64 -I/usr/include/apr-1.0 binarytrees.gcc-3.c -o binarytrees.gcc-3.gcc_run -lapr-1 -lgomp -lm

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./binarytrees.gcc-3.gcc_run 21

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./binarytrees.gcc-3.gcc_run 21
