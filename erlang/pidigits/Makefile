compile:
	cp pidigits.hipe pidigits.erl
	${COMPILER} +native +"{hipe, [o3]}" pidigits.erl
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} -smp enable -noshell -run  pidigits main 10000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ${BINARY} -smp enable -noshell -run  pidigits main 10000

