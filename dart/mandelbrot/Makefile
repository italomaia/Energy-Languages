compile:

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/bin/dart  mandelbrot.dart 16000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/bin/dart  mandelbrot.dart 16000

