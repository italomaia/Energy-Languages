compile:
	CGO_ENABLED=0 ${COMPILER} build spectralnorm.go

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./spectralnorm 5500

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./spectralnorm 5500

