compile:

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/bin/dart  fannkuchredux.dart-2.dart 12

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/bin/dart  fannkuchredux.dart-2.dart 12

