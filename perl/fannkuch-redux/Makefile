compile:

measure:
	sudo modprobe msr
	sudo /opt/rapl/main "${BINARY} fannkuchredux.perl-2.perl 12" Perl fannkuch-redux

run:
	${BINARY} fannkuchredux.perl-2.perl 12

mem:
	/usr/bin/time -v ${BINARY} fannkuchredux.perl-2.perl 12

valgrind:
	valgrind --tool=massif --stacks=yes ${BINARY} fannkuchredux.perl-2.perl 12
