compile:

measure:
	/opt/rapl/main "/usr/bin/dart --old_gen_heap_size=2048 revcomp.dart-3.dart 0 < /root/data/revcomp-input25000000.txt" Dart reverse-complement

run:
	/usr/bin/dart --old_gen_heap_size=2048 revcomp.dart-3.dart 0 < /root/data/revcomp-input25000000.txt

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/bin/dart --old_gen_heap_size=2048 revcomp.dart-3.dart 0 < /root/data/revcomp-input25000000.txt

valgrind:
	valgrind --tool=massif --stacks=yes /usr/bin/dart --old_gen_heap_size=2048 revcomp.dart-3.dart 0 < /root/data/revcomp-input25000000.txt
