compile:
	CGO_ENABLED=0 ${COMPILER} build nbody.go

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./nbody 50000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./nbody 50000000

