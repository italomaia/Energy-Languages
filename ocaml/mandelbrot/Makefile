compile:
	cp mandelbrot.ocaml mandelbrot.ml
	${COMPILER} -noassert -unsafe -fPIC -nodynlink -inline 100 unix.cmxa mandelbrot.ml -o mandelbrot.ocaml_run
	rm mandelbrot.ml

run:
	./mandelbrot.ocaml_run 16000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./mandelbrot.ocaml_run 16000

