compile:
	cp binarytrees.hipe-2.hipe binarytrees.erl
	${COMPILER} +native +"{hipe, [o3]}" binarytrees.erl
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} -smp enable -noshell -run  binarytrees main 21

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ${BINARY} -smp enable -noshell -run  binarytrees main 21

