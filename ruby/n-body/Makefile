compile:


measure:
	/opt/rapl/main "${BINARY} -W0 nbody.yarv-2.yarv 50000000" Ruby n-body

run:
	${BINARY} -W0 nbody.yarv-2.yarv 50000000

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -W0 nbody.yarv-2.yarv 50000000

valgrind:
	valgrind --tool=massif --stacks=yes ${BINARY} -W0 nbody.yarv-2.yarv 50000000
