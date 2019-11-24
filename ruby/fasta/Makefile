compile:


measure:
	/opt/rapl/main "${BINARY} -W0 fasta.yarv-3.yarv 25000000" Ruby fasta

run:
	${BINARY} -W0 fasta.yarv-3.yarv 25000000

mem:
	/usr/bin/time -v  ${BINARY} -W0 fasta.yarv-3.yarv 25000000

valgrind:
	valgrind --tool=massif --stacks=yes  ${BINARY} -W0 fasta.yarv-3.yarv 25000000
