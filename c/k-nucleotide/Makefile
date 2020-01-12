compile:
	/usr/bin/gcc -pipe -Wall -O3 -fomit-frame-pointer -march=native -fopenmp -std=c99 -IInclude knucleotide.c -o knucleotide.gcc_run
run:
	./knucleotide.gcc_run 0 < /root/data/knucleotide-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./knucleotide.gcc_run 0 < /root/data/knucleotide-input25000000.txt
