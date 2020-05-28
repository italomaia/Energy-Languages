compile:


prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} -W0 fannkuchredux.yarv-2.yarv 12

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -W0 fannkuchredux.yarv-2.yarv 12

