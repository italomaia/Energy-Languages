compile:

measure:
	/opt/rapl/main "${BINARY} fasta.perl 25000000" Perl fasta

run:
	${BINARY} fasta.perl 25000000
mem:
	/usr/bin/time -v ${BINARY} fasta.perl 25000000

valgrind:
	valgrind --tool=massif --stacks=yes ${BINARY} fasta.perl 25000000

