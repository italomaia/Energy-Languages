compile:
	/usr/bin/gcc -pipe -Wall -O3 -fomit-frame-pointer -march=native -pthread chameneosredux.gcc-5.c -o chameneosredux.gcc-5.gcc_run

measure:
	/opt/rapl/main "./chameneosredux.gcc-5.gcc_run 6000000"

run:
	./chameneosredux.gcc-5.gcc_run 6000000
mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./chameneosredux.gcc-5.gcc_run 6000000
