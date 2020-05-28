compile:
	cp spectralnorm.hipe-2.hipe spectralnorm.erl
	${COMPILER} +native +"{hipe, [o3]}" spectralnorm.erl
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} -smp enable -noshell -run  spectralnorm main 5500

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -smp enable -noshell -run  spectralnorm main 5500

