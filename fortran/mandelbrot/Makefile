compile:
	ifort -O3 -fast -qopenmp mandelbrot.ifc-4.f90 -o mandelbrot.ifc-4.ifc_run
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./mandelbrot.ifc-4.ifc_run 16000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./mandelbrot.ifc-4.ifc_run 16000

