compile:


measure:
	sudo modprobe msr
	sudo /opt/rapl/main "${BINARY} -W0 nbody.yarv-2.yarv 50000000" Ruby n-body

run:
	${BINARY} -W0 nbody.yarv-2.yarv 50000000

mem:
	/usr/bin/time -v ${BINARY} -W0 nbody.yarv-2.yarv 50000000

valgrind:
	valgrind --tool=massif --stacks=yes ${BINARY} -W0 nbody.yarv-2.yarv 50000000
