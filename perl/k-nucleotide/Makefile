compile:

measure:
	sudo modprobe msr
	sudo /opt/rapl/main "${BINARY} knucleotide.perl 0 < knucleotide-input25000000.txt" Perl k-nucleotide

run:
	${BINARY} knucleotide.perl 0 < knucleotide-input25000000.txt

mem:
	/usr/bin/time -v ${BINARY} knucleotide.perl 0 < knucleotide-input25000000.txt

valgrind:
	valgrind --tool=massif --stacks=yes ${BINARY} knucleotide.perl 0 < knucleotide-input25000000.txt
