compile:
	cp fasta.fpascal-4.fpascal fasta.fpascal-4.pas
	/usr/local/src/fpc-3.0.2.x86_64-linux/bin/fpc -FuInclude/fpascal -XXs -O4 -Tlinux -oFPASCAL_RUN fasta.fpascal-4.pas
	mv FPASCAL_RUN fasta.fpascal-4.fpascal_run
	rm fasta.fpascal-4.pas

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./fasta.fpascal-4.fpascal_run 25000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./fasta.fpascal-4.fpascal_run 25000000

