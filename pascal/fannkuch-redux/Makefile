compile:
	cp fannkuchredux.fpascal fannkuchredux.pas
	/usr/local/src/fpc-3.0.2.x86_64-linux/bin/fpc -FuInclude/fpascal -XXs -O4 -Tlinux -oFPASCAL_RUN fannkuchredux.pas
	mv FPASCAL_RUN fannkuchredux.fpascal_run
	rm fannkuchredux.pas
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./fannkuchredux.fpascal_run 12

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./fannkuchredux.fpascal_run 12


