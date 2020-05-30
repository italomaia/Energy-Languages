compile:
	${BINARY} build -c Release

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} ./bin/Release/netcoreapp1.1/tmp.dll 6000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} ./bin/Release/netcoreapp1.1/tmp.dll 6000000

