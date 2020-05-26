compile:
	cp nbody.hipe-3.hipe nbody.erl
	${COMPILER} +native +"{hipe, [o3]}" nbody.erl
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} -smp enable -noshell -run  nbody main 50000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ${BINARY} -smp enable -noshell -run  nbody main 50000000

