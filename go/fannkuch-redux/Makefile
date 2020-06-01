compile:
	CGO_ENABLED=0 ${COMPILER} build fannkuchredux.go

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./fannkuchredux 12

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./fannkuchredux 12

