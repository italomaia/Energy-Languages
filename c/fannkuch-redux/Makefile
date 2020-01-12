compile:
	/usr/bin/gcc -pipe -Wall -O3 -fomit-frame-pointer -march=native -std=c99 -fopenmp fannkuchredux.gcc-5.c -o fannkuchredux.gcc-5.gcc_run

measure:
	/opt/rapl/main "./fannkuchredux.gcc-5.gcc_run 12" C fannkuch-redux

run:
	./fannkuchredux.gcc-5.gcc_run 12

mem:
	 /usr/bin/time -o /opt/measures/${TLANG}.txt -v ./fannkuchredux.gcc-5.gcc_run 12
