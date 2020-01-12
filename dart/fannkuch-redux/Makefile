compile:

measure:
	/opt/rapl/main "/usr/bin/dart  fannkuchredux.dart-2.dart 12" Dart fannkuch-redux

run:
	/usr/bin/dart  fannkuchredux.dart-2.dart 12

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/bin/dart  fannkuchredux.dart-2.dart 12

valgrind:
	valgrind --tool=massif --stacks=yes /usr/bin/dart  fannkuchredux.dart-2.dart 12
