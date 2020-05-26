compile:
	/usr/bin/gcc -pipe -Wall -O3 -fomit-frame-pointer -march=native -funroll-loops -fopenmp revcomp.gcc-6.c -o revcomp.gcc-6.gcc_run
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./revcomp.gcc-6.gcc_run 0 < /root/data/revcomp-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./revcomp.gcc-6.gcc_run 0 < /root/data/revcomp-input25000000.txt
