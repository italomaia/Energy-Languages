compile:
	cp fannkuchredux.hipe fannkuchredux.erl
	${COMPILER} +native +"{hipe, [o3]}" fannkuchredux.erl
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} -smp enable -noshell -run  fannkuchredux main 12

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -smp enable -noshell -run  fannkuchredux main 12

