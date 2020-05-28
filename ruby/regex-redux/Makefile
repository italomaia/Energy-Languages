compile:i


prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} -W0 regexredux.yarv-2.yarv 0 < /root/data/regexredux-input5000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -W0 regexredux.yarv-2.yarv 0 < /root/data/regexredux-input5000000.txt

