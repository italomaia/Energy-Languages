compile:

measure:
	sudo modprobe msr
	sudo /opt/rapl/main "${BINARY} nbody.perl-2.perl 50000000" Perl n-body

run:
	${BINARY} nbody.perl-2.perl 50000000

mem:
	/usr/bin/time -v ${BINARY} nbody.perl-2.perl 50000000

valgrind:
	valgrind --tool=massif --stacks=yes ${BINARY} nbody.perl-2.perl 50000000
