compile:
	/usr/bin/gcc -pipe -Wall -O3 -fomit-frame-pointer -march=native -std=c99 -fopenmp fannkuchredux.gcc-5.c -o fannkuchredux.gcc-5.gcc_run

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./fannkuchredux.gcc-5.gcc_run 12 > /opt/results/${TLANG}/${TEST_NAME}.txt

measure:
	 /usr/bin/time -o /opt/measures/${TLANG}.txt -v ./fannkuchredux.gcc-5.gcc_run 12
