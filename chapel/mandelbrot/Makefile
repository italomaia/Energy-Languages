compile:
	/usr/local/src/chapel-1.15.0/bin/linux64/chpl --fast mandelbrot.chapel-2.chpl -o mandelbrot.chapel-2.chapel_run
run:
	./mandelbrot.chapel-2.chapel_run --n=16000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./mandelbrot.chapel-2.chapel_run --n=16000

