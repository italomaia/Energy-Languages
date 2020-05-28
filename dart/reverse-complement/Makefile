compile:

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/bin/dart --old_gen_heap_size=2048 revcomp.dart-3.dart 0 < /root/data/revcomp-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/bin/dart --old_gen_heap_size=2048 revcomp.dart-3.dart 0 < /root/data/revcomp-input25000000.txt

