compile:
	${COMPILER} build -o pidigits.go-3.go_run

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./pidigits.go-3.go_run 10000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./pidigits.go-3.go_run 10000

