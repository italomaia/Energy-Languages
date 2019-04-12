BINARY=/usr/bin/lua5.3

compile:

measure:
	sudo modprobe msr
	sudo ../../RAPL/main "${BINARY}  fannkuchredux.lua 12" Lua fannkuch-redux

run:
	${BINARY}  fannkuchredux.lua 12

mem:
	/usr/bin/time -v ${BINARY}  fannkuchredux.lua 12

valgrind:
	valgrind --tool=massif --stacks=yes ${BINARY}  fannkuchredux.lua 12
