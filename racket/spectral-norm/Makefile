compile:
	/usr/local/src/racket-6.8/bin/raco make spectralnorm.racket-3.racket

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/local/src/racket-6.8/bin/racket ./compiled/spectralnorm.racket-3_racket.zo 5500

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/racket-6.8/bin/racket ./compiled/spectralnorm.racket-3_racket.zo 5500

