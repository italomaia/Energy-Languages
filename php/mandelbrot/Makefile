compile:

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	php  mandelbrot.php-3.php 16000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v php  mandelbrot.php-3.php 16000

