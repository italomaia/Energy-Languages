compile:

measure:
	/opt/rapl/main "/usr/bin/dart  mandelbrot.dart 16000" Dart mandelbrot

run:
	/usr/bin/dart  mandelbrot.dart 16000

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/bin/dart  mandelbrot.dart 16000

valgrind:
	valgrind --tool=massif --stacks=yes /usr/bin/dart  mandelbrot.dart 16000
