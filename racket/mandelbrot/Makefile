compile:
	/usr/local/src/racket-6.8/bin/raco make mandelbrot.racket-3.racket

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/local/src/racket-6.8/bin/racket ./compiled/mandelbrot.racket-3_racket.zo 16000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/racket-6.8/bin/racket ./compiled/mandelbrot.racket-3_racket.zo 16000

