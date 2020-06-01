compile:
	CGO_ENABLED=0 ${COMPILER} build revcomp.go

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./revcomp 0 < /root/data/revcomp-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v   ./revcomp 0 < /root/data/revcomp-input25000000.txt

