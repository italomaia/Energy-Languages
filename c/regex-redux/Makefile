compile:
	/usr/bin/gcc -pipe -Wall -O3 -fomit-frame-pointer -march=native -fopenmp regexredux.gcc-4.c -o regexredux.gcc-4.gcc_run -lpcre

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./regexredux.gcc-4.gcc_run 0 < /root/data/regexredux-input5000000.txt
measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./regexredux.gcc-4.gcc_run 0 < /root/data/regexredux-input5000000.txt
