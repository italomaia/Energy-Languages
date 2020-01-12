compile:

measure:
	/opt/rapl/main "/usr/bin/dart  nbody.dart-3.dart 50000000" Dart n-body

run:
	/usr/bin/dart  nbody.dart-3.dart 50000000

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/bin/dart  nbody.dart-3.dart 50000000

valgrind:
	valgrind --tool=massif --stacks=yes /usr/bin/dart  nbody.dart-3.dart 50000000
