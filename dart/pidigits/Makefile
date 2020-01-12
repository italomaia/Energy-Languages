compile:

xmeasure:
	/opt/rapl/main "/usr/bin/dart  pidigits.dart 2000" Dart pidigits

run:
	/usr/bin/dart  pidigits.dart 2000

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  /usr/bin/dart  pidigits.dart 2000

valgrind:
	valgrind --tool=massif --stacks=yes  /usr/bin/dart  pidigits.dart 2000
