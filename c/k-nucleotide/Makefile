compile:
	/usr/bin/gcc -pipe -Wall -O3 -fomit-frame-pointer -march=native -fopenmp -std=c99 -I/root/libs/htslib -IInclude knucleotide.c -o knucleotide.gcc_run

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./knucleotide.gcc_run 0 < /root/data/knucleotide-input25000000.txt > /opt/results/${TLANG}/${TEST_NAME}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./knucleotide.gcc_run 0 < /root/data/knucleotide-input25000000.txt
