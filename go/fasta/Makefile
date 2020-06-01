compile:
	CGO_ENABLED=0 ${COMPILER} build fasta.go

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./fasta 25000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./fasta 25000000

