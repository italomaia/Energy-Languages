compile:
	/usr/local/src/racket-6.8/bin/raco make fasta.racket-3.racket

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/local/src/racket-6.8/bin/racket ./compiled/fasta.racket-3_racket.zo 25000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/racket-6.8/bin/racket ./compiled/fasta.racket-3_racket.zo 25000000

