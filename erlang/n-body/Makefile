compile:
	cp nbody.hipe-3.hipe nbody.erl
	${COMPILER} +native +"{hipe, [o3]}" nbody.erl
measure:
	sudo modprobe msr
	sudo /opt/rapl/main "${BINARY} -smp enable -noshell -run  nbody main 50000000" Erlang n-body

run:
	${BINARY} -smp enable -noshell -run  nbody main 50000000

mem:
	/usr/bin/time -v  ${BINARY} -smp enable -noshell -run  nbody main 50000000

valgrind:
	valgrind --tool=massif --stacks=yes  ${BINARY} -smp enable -noshell -run  nbody main 50000000
