compile:


xprepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} -W0 pidigits.yarv-5.yarv 10000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ${BINARY} -W0 pidigits.yarv-5.yarv 10000

