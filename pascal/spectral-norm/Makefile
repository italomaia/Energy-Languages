compile:
	cp spectralnorm.fpascal-2.fpascal spectralnorm.fpascal-2.pas
	/usr/local/src/fpc-3.0.2.x86_64-linux/bin/fpc -FuInclude/fpascal -XXs -O4 -Tlinux -Fi Include/fpascal -oFPASCAL_RUN spectralnorm.fpascal-2.pas
	mv FPASCAL_RUN spectralnorm.fpascal-2.fpascal_run
	rm spectralnorm.fpascal-2.pas
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./spectralnorm.fpascal-2.fpascal_run 5500

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./spectralnorm.fpascal-2.fpascal_run 5500

