compile:
	cp regexredux.hipe-6.hipe regexredux.erl
	${COMPILER} +native +"{hipe, [o3]}" regexredux.erl
xmeasure:
	/opt/rapl/main "${BINARY} -smp enable -noshell -run -noinput -run regexredux main 0 < ../../regexredux-input50000.txt" Erlang regex-redux

run:
	${BINARY} -smp enable -noshell -run -noinput -run regexredux main 0 < ../../regexredux-input50000.txt

mem:
	/usr/bin/time -v  ${BINARY} -smp enable -noshell -run -noinput -run regexredux main 0 < ../../regexredux-input50000.txt

valgrind:
	valgrind --tool=massif --stacks=yes  ${BINARY} -smp enable -noshell -run -noinput -run regexredux main 0 < ../../regexredux-input50000.txt
