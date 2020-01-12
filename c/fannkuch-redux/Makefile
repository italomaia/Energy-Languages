compile:
	/usr/bin/gcc -pipe -Wall -O3 -fomit-frame-pointer -march=native -std=c99 -fopenmp fannkuchredux.gcc-5.c -o fannkuchredux.gcc-5.gcc_run

run:
	./fannkuchredux.gcc-5.gcc_run 12

measure:
	 /usr/bin/time -o /opt/measures/${TLANG}.txt -v ./fannkuchredux.gcc-5.gcc_run 12
