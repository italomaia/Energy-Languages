compile:

measure:
	sudo /opt/rapl/main "${BINARY} binarytrees.perl-3.perl 21" Perl binary-trees

run:
	${BINARY} binarytrees.perl-3.perl 21

mem:
	/usr/bin/time -v  ${BINARY} binarytrees.perl-3.perl 21

valgrind:
	valgrind --tool=massif --stacks=yes  ${BINARY} binarytrees.perl-3.perl 21
