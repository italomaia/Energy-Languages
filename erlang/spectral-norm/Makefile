compile:
	cp spectralnorm.hipe-2.hipe spectralnorm.erl
	${COMPILER} +native +"{hipe, [o3]}" spectralnorm.erl
measure:
	/opt/rapl/main "${BINARY} -smp enable -noshell -run  spectralnorm main 5500" Erlang spectral-norm

run:
	${BINARY} -smp enable -noshell -run  spectralnorm main 5500

mem:
	/usr/bin/time -v ${BINARY} -smp enable -noshell -run  spectralnorm main 5500

valgrind:
	valgrind --tool=massif --stacks=yes ${BINARY} -smp enable -noshell -run  spectralnorm main 5500
