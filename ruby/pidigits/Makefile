compile:


xmeasure:
	/opt/rapl/main "${BINARY} -W0 pidigits.yarv-5.yarv 10000" Ruby pidigits

run:
	${BINARY} -W0 pidigits.yarv-5.yarv 10000

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ${BINARY} -W0 pidigits.yarv-5.yarv 10000

valgrind:
	valgrind --tool=massif --stacks=yes  ${BINARY} -W0 pidigits.yarv-5.yarv 10000
