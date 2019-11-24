compile:

measure:
	/opt/rapl/main "/usr/bin/dart  spectralnorm.dart 5500" Dart spectral-norm

run:
	/usr/bin/dart  spectralnorm.dart 5500

mem:
	/usr/bin/time -v /usr/bin/dart  spectralnorm.dart 5500

valgrind:
	valgrind --tool=massif --stacks=yes /usr/bin/dart  spectralnorm.dart 5500
