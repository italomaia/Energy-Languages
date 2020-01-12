compile:

measure:
	/opt/rapl/main "/usr/bin/dart  regexredux.dart-2.dart 0 < /root/data/regexredux-input5000000.txt" Dart regex-redux

run:
	/usr/bin/dart  regexredux.dart-2.dart 0 < /root/data/regexredux-input5000000.txt

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  /usr/bin/dart  regexredux.dart-2.dart 0 < /root/data/regexredux-input5000000.txt

valgrind:
	valgrind --tool=massif --stacks=yes  /usr/bin/dart  regexredux.dart-2.dart 0 < /root/data/regexredux-input5000000.txt
