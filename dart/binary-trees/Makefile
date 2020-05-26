compile:

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/bin/dart  binarytrees.dart 21

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  /usr/bin/dart  binarytrees.dart 21

