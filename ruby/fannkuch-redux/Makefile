compile:


measure:
	/opt/rapl/main "${BINARY} -W0 fannkuchredux.yarv-2.yarv 12" Ruby fannkuch-redux

run:
	${BINARY} -W0 fannkuchredux.yarv-2.yarv 12

mem:
	/usr/bin/time -v ${BINARY} -W0 fannkuchredux.yarv-2.yarv 12

valgrind:
	valgrind --tool=massif --stacks=yes ${BINARY} -W0 fannkuchredux.yarv-2.yarv 12
