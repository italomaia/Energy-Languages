compile:
	CGO_ENABLED=0 ${COMPILER} build knucleotide.go

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./knucleotide 0 < /root/data/knucleotide-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./knucleotide 0 < /root/data/knucleotide-input25000000.txt

