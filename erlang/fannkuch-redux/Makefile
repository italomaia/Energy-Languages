compile:
	cp fannkuchredux.hipe fannkuchredux.erl
	${COMPILER} +native +"{hipe, [o3]}" fannkuchredux.erl
measure:
	/opt/rapl/main "${BINARY} -smp enable -noshell -run  fannkuchredux main 12" Erlang fannkuch-redux

run:
	${BINARY} -smp enable -noshell -run  fannkuchredux main 12

mem:
	/usr/bin/time -v ${BINARY} -smp enable -noshell -run  fannkuchredux main 12

valgrind:
	valgrind --tool=massif --stacks=yes ${BINARY} -smp enable -noshell -run  fannkuchredux main 12
