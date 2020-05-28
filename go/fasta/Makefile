compile:
	/usr/bin/go build -o fasta.go-3.go_run

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./fasta.go-3.go_run 25000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./fasta.go-3.go_run 25000000

