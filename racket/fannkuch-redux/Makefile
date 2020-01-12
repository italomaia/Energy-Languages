compile:
	/usr/local/src/racket-6.8/bin/raco make fannkuchredux.racket-3.racket

measure:
	/opt/rapl/main "/usr/local/src/racket-6.8/bin/racket ./compiled/fannkuchredux.racket-3_racket.zo 12" Racket fannkuch-redux

run:
	/usr/local/src/racket-6.8/bin/racket ./compiled/fannkuchredux.racket-3_racket.zo 12

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/racket-6.8/bin/racket ./compiled/fannkuchredux.racket-3_racket.zo 12

valgrind:
	valgrind --tool=massif --stacks=yes /usr/local/src/racket-6.8/bin/racket ./compiled/fannkuchredux.racket-3_racket.zo 12
