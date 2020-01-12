compile:
	/usr/bin/gcc -pipe -Wall -O3 -fomit-frame-pointer -march=native  pidigits.c -o pidigits.gcc_run -lgmp
run:
	./pidigits.gcc_run 10000
measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./pidigits.gcc_run 10000
