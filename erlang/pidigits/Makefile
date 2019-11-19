compile:
	cp pidigits.hipe pidigits.erl
	${COMPILER} +native +"{hipe, [o3]}" pidigits.erl
measure:
	sudo modprobe msr
	sudo /opt/rapl/main "${BINARY} -smp enable -noshell -run  pidigits main 10000" Erlang pidigits

run:
	${BINARY} -smp enable -noshell -run  pidigits main 10000

mem:
	/usr/bin/time -v  ${BINARY} -smp enable -noshell -run  pidigits main 10000

valgrind:
	valgrind --tool=massif --stacks=yes  ${BINARY} -smp enable -noshell -run  pidigits main 10000
