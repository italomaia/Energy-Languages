compile:
	/usr/bin/gcc -pipe -Wall -O3 -fomit-frame-pointer -march=native  pidigits.c -o pidigits.gcc_run -lgmp
measure:
	/opt/rapl/main "./pidigits.gcc_run 10000" C pidigits

run:
	./pidigits.gcc_run 10000
mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./pidigits.gcc_run 10000
