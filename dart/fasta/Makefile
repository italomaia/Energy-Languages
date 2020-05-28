compile:

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/bin/dart  fasta.dart 25000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  /usr/bin/dart  fasta.dart 25000000

