compile:
	CGO_ENABLED=0 ${COMPILER} build regexredux.go

xprepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./regexredux 0 < /root/data/regexredux-input5000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./regexredux 0 < /root/data/regexredux-input5000000.txt

