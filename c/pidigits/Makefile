compile:
	/usr/bin/gcc -pipe -Wall -O3 -fomit-frame-pointer -march=native  pidigits.c -o pidigits.gcc_run -lgmp

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./pidigits.gcc_run 10000 > /opt/results/${TLANG}/${TEST_NAME}.txt
measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./pidigits.gcc_run 10000
