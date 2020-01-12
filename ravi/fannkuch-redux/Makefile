BINARY=/usr/bin/ravi

compile:

measure:
	/opt/rapl/main "${BINARY} fannkuchredux.lua 12" Lua fannkuch-redux

run:
	${BINARY} fannkuchredux.lua 12

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} fannkuchredux.lua 12

valgrind:
	valgrind --tool=massif --stacks=yes ${BINARY} fannkuchredux.lua 12
