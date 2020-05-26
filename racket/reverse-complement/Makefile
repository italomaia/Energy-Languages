compile:
	/usr/local/src/racket-6.8/bin/raco make revcomp.racket-2.racket

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/local/src/racket-6.8/bin/racket ./compiled/revcomp.racket-2_racket.zo 0 < /root/data/revcomp-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/racket-6.8/bin/racket ./compiled/revcomp.racket-2_racket.zo 0 < /root/data/revcomp-input25000000.txt

