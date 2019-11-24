compile:
	cp binarytrees.hipe-2.hipe binarytrees.erl
	${COMPILER} +native +"{hipe, [o3]}" binarytrees.erl
measure:
	sudo /opt/rapl/main "${BINARY} -smp enable -noshell -run  binarytrees main 21" Erlang binary-trees

run:
	${BINARY} -smp enable -noshell -run  binarytrees main 21

mem:
	/usr/bin/time -v  ${BINARY} -smp enable -noshell -run  binarytrees main 21

valgrind:
	valgrind --tool=massif --stacks=yes  ${BINARY} -smp enable -noshell -run  binarytrees main 21
