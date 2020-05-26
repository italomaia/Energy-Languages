compile:
	/usr/bin/gcc -pipe -Wall -O3 -fomit-frame-pointer -march=native -pthread chameneosredux.gcc-5.c -o chameneosredux.gcc-5.gcc_run

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./chameneosredux.gcc-5.gcc_run 6000000
measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./chameneosredux.gcc-5.gcc_run 6000000
