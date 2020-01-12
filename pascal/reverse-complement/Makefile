compile:
	cp revcomp.fpascal-2.fpascal revcomp.fpascal-2.pas
	/usr/local/src/fpc-3.0.2.x86_64-linux/bin/fpc -FuInclude/fpascal -XXs -O4 -Tlinux -oFPASCAL_RUN revcomp.fpascal-2.pas
	mv FPASCAL_RUN revcomp.fpascal-2.fpascal_run
	rm revcomp.fpascal-2.pas
run:
	./revcomp.fpascal-2.fpascal_run 0 < /root/data/revcomp-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./revcomp.fpascal-2.fpascal_run 0 < /root/data/revcomp-input25000000.txt

