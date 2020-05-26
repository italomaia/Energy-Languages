compile:
	/usr/local/src/racket-6.8/bin/raco make fannkuchredux.racket-3.racket

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/local/src/racket-6.8/bin/racket ./compiled/fannkuchredux.racket-3_racket.zo 12

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/racket-6.8/bin/racket ./compiled/fannkuchredux.racket-3_racket.zo 12

