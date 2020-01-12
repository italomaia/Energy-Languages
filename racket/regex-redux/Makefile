compile:
	/usr/local/src/racket-6.8/bin/raco make regexredux.racket

measure:
	/opt/rapl/main "/usr/local/src/racket-6.8/bin/racket ./compiled/regexredux_racket.zo 0 < /root/data/regexredux-input5000000.txt" Racket regex-redux

run:
	/usr/local/src/racket-6.8/bin/racket ./compiled/regexredux_racket.zo 0 < /root/data/regexredux-input5000000.txt

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/racket-6.8/bin/racket ./compiled/regexredux_racket.zo 0 < /root/data/regexredux-input5000000.txt

valgrind:
	valgrind --tool=massif --stacks=yes /usr/local/src/racket-6.8/bin/racket ./compiled/regexredux_racket.zo 0 < /root/data/regexredux-input5000000.txt
