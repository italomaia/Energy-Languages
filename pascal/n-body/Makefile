compile:
	cp nbody.fpascal nbody.pas
	/usr/local/src/fpc-3.0.2.x86_64-linux/bin/fpc -FuInclude/fpascal -XXs -O4 -Tlinux -CfSSE3 -oFPASCAL_RUN nbody.pas
	mv FPASCAL_RUN nbody.fpascal_run
	rm nbody.pas

run:
	./nbody.fpascal_run 50000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./nbody.fpascal_run 50000000

