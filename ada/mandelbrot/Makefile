compile:
	gnatchop -r -w mandelbrot.gnat-3.gnat
	gnatmake -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp -f mandelbrot.adb -o mandelbrot.gnat-3.gnat_run
	gcc-6 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp mandelbrot.adb
	gnatbind-6 -x mandelbrot.ali
	gnatlink-6 mandelbrot.ali -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -o mandelbrot.gnat-3.gnat_run
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./mandelbrot.gnat-3.gnat_run 16000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./mandelbrot.gnat-3.gnat_run 16000

