compile:
	/usr/local/src/racket-6.8/bin/raco make regexredux.racket

run:
	/usr/local/src/racket-6.8/bin/racket ./compiled/regexredux_racket.zo 0 < /root/data/regexredux-input5000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/racket-6.8/bin/racket ./compiled/regexredux_racket.zo 0 < /root/data/regexredux-input5000000.txt

