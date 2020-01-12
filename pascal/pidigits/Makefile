compile:
	cp pidigits.fpascal-3.fpascal pidigits.fpascal-3.pas
	/usr/local/src/fpc-3.0.2.x86_64-linux/bin/fpc -FuInclude/fpascal -XXs -O4 -Tlinux -oFPASCAL_RUN pidigits.fpascal-3.pas
	mv FPASCAL_RUN pidigits.fpascal-3.fpascal_run
	rm pidigits.fpascal-3.pas
run:
	./pidigits.fpascal-3.fpascal_run 10000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./pidigits.fpascal-3.fpascal_run 10000

