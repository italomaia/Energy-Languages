compile:
	${COMPILER} build pidigits.go

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./pidigits 10000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./pidigits 10000

