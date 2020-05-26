compile:
	cp mandelbrot.fpascal-5.fpascal mandelbrot.fpascal-5.pas
	/usr/local/src/fpc-3.0.2.x86_64-linux/bin/fpc -FuInclude/fpascal -XXs -O4 -Tlinux  -oFPASCAL_RUN mandelbrot.fpascal-5.pas
	mv FPASCAL_RUN mandelbrot.fpascal-5.fpascal_run
	rm mandelbrot.fpascal-5.pas

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./mandelbrot.fpascal-5.fpascal_run 16000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./mandelbrot.fpascal-5.fpascal_run 16000

