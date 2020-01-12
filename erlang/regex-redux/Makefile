compile:
	cp regexredux.hipe-6.hipe regexredux.erl
	${COMPILER} +native +"{hipe, [o3]}" regexredux.erl
xrun:
	${BINARY} -smp enable -noshell -run -noinput -run regexredux main 0 < ../../regexredux-input50000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ${BINARY} -smp enable -noshell -run -noinput -run regexredux main 0 < ../../regexredux-input50000.txt

