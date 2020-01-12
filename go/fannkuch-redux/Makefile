compile:
	/usr/bin/go build -o fannkuchredux.go_run

measure:
	/opt/rapl/main "./fannkuchredux.go_run 12" Go fannkuch-redux

run:
	./fannkuchredux.go_run 12

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./fannkuchredux.go_run 12

valgrind:
	valgrind --tool=massif --stacks=yes ./fannkuchredux.go_run 12
