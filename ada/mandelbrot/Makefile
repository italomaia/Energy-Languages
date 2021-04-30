compile:
	gnatchop -r -w mandelbrot.gnat-3.gnat
	gnatmake -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp -f mandelbrot.adb -o mandelbrot.gnat-3.gnat_run
	gcc -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp mandelbrot.adb
	gnatbind -x mandelbrot.ali
	gnatlink mandelbrot.ali -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -o mandelbrot.gnat-3.gnat_run
	chmod a+x /root/${TEST_NAME}/*.gnat_run

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./mandelbrot.gnat-3.gnat_run 16000 > /opt/results/${TLANG}/${TEST_NAME}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./mandelbrot.gnat-3.gnat_run 16000

