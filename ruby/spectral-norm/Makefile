compile:


prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} -W0 spectralnorm.yarv-5.yarv 5500

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -W0 spectralnorm.yarv-5.yarv 5500


