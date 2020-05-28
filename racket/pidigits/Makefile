compile:
	/usr/local/src/racket-6.8/bin/raco make pidigits.racket-2.racket

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/local/src/racket-6.8/bin/racket ./compiled/pidigits.racket-2_racket.zo 10000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/racket-6.8/bin/racket ./compiled/pidigits.racket-2_racket.zo 10000

