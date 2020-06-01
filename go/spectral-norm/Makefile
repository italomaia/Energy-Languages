compile:
	${COMPILER} build -o spectralnorm.go-4.go_run

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./spectralnorm.go-4.go_run 5500

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./spectralnorm.go-4.go_run 5500

