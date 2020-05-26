compile:

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/bin/dart  regexredux.dart-2.dart 0 < /root/data/regexredux-input5000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  /usr/bin/dart  regexredux.dart-2.dart 0 < /root/data/regexredux-input5000000.txt

