compile:
	/usr/local/src/racket-6.8/bin/raco make nbody.racket-2.racket

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/local/src/racket-6.8/bin/racket ./compiled/nbody.racket-2_racket.zo 50000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  /usr/local/src/racket-6.8/bin/racket ./compiled/nbody.racket-2_racket.zo 50000000

