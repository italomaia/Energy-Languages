compile:
	cp fasta.hipe-2.hipe fasta.erl
	${COMPILER} +native +"{hipe, [o3]}" fasta.erl
measure:
	sudo modprobe msr
	sudo /opt/rapl/main "${BINARY} -smp enable -noshell -run  fasta main 25000000" Erlang fasta

run:
	${BINARY} -smp enable -noshell -run  fasta main 25000000

mem:
	/usr/bin/time -v ${BINARY} -smp enable -noshell -run  fasta main 25000000
valgrind:
	valgrind --tool=massif --stacks=yes ${BINARY} -smp enable -noshell -run  fasta main 25000000
