compile:
	${COMPILER} build -o knucleotide.go-6.go_run

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./knucleotide.go-6.go_run 0 < /root/data/knucleotide-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./knucleotide.go-6.go_run 0 < /root/data/knucleotide-input25000000.txt

