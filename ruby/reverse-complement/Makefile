compile:


measure:
	/opt/rapl/main "${BINARY} -W0 revcomp.yarv-3.yarv 0 < /root/data/revcomp-input25000000.txt" Ruby reverse-complement

run:
	${BINARY} -W0 revcomp.yarv-3.yarv 0 < /root/data/revcomp-input25000000.txt

mem:
	/usr/bin/time -v ${BINARY} -W0 revcomp.yarv-3.yarv 0 < /root/data/revcomp-input25000000.txt

valgrind:
	valgrind --tool=massif --stacks=yes ${BINARY} -W0 revcomp.yarv-3.yarv 0 < /root/data/revcomp-input25000000.txt
