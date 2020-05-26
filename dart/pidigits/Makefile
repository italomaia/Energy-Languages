compile:

xprepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/bin/dart  pidigits.dart 2000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  /usr/bin/dart  pidigits.dart 2000

