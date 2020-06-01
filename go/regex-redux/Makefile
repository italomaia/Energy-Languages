compile:
	${COMPILER} build -o regexredux.go-2.go_run

xprepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./regexredux.go-2.go_run 0 < /root/data/regexredux-input5000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./regexredux.go-2.go_run 0 < /root/data/regexredux-input5000000.txt

