compile:
	${COMPILER} build -o revcomp.go-6.go_run

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./revcomp.go-6.go_run 0 < /root/data/revcomp-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v   ./revcomp.go-6.go_run 0 < /root/data/revcomp-input25000000.txt

