compile:


measure:
	/opt/rapl/main "${BINARY} -W0 spectralnorm.yarv-5.yarv 5500" Ruby spectral-norm

run:
	${BINARY} -W0 spectralnorm.yarv-5.yarv 5500

mem:
	/usr/bin/time -v ${BINARY} -W0 spectralnorm.yarv-5.yarv 5500

valgrind:
	valgrind --tool=massif --stacks=yes ${BINARY} -W0 spectralnorm.yarv-5.yarv 5500

