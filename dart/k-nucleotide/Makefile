compile:

measure:
	/opt/rapl/main "/usr/bin/dart  knucleotide.dart-2.dart 0 < /root/data/knucleotide-input25000000.txt" Dart k-nucleotide

run:
	/usr/bin/dart  knucleotide.dart-2.dart 0 < /root/data/knucleotide-input25000000.txt

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  /usr/bin/dart  knucleotide.dart-2.dart 0 < /root/data/knucleotide-input25000000.txt

valgrind:
	valgrind --tool=massif --stacks=yes  /usr/bin/dart  knucleotide.dart-2.dart 0 < /root/data/knucleotide-input25000000.txt
