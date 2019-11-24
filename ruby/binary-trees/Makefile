compile:


measure:
	sudo /opt/rapl/main "${BINARY} -W0 binarytrees.yarv-5.yarv 21" Ruby binary-trees

run:
	${BINARY} -W0 binarytrees.yarv-5.yarv 21

mem:
	/usr/bin/time -v ${BINARY} -W0 binarytrees.yarv-5.yarv 21

valgrind:
	valgrind --tool=massif --stacks=yes ${BINARY} -W0 binarytrees.yarv-5.yarv 21
