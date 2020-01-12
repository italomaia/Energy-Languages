compile:
	/usr/bin/gcc -pipe -Wall -O3 -fomit-frame-pointer -march=native -std=c99 -mfpmath=sse -msse3 -fopenmp fasta.gcc-2.c -o fasta.gcc-2.gcc_run

measure:
	/opt/rapl/main "./fasta.gcc-2.gcc_run 25000000" C fasta

run:
	./fasta.gcc-2.gcc_run 25000000

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./fasta.gcc-2.gcc_run 25000000
