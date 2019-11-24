compile:
	cp revcomp.hipe revcomp.erl
	${COMPILER} +native +"{hipe, [o3]}" revcomp.erl
measure:
	sudo /opt/rapl/main "${BINARY} -smp enable -noshell -run  revcomp main 0 < /root/data/revcomp-input25000000.txt" Erlang reverse-complement

run:
	${BINARY} -smp enable -noshell -run  revcomp main 0 < /root/data/revcomp-input25000000.txt

mem:
	/usr/bin/time -v ${BINARY} -smp enable -noshell -run  revcomp main 0 < /root/data/revcomp-input25000000.txt

valgrind:
	valgrind --tool=massif --stacks=yes ${BINARY} -smp enable -noshell -run  revcomp main 0 < /root/data/revcomp-input25000000.txt
