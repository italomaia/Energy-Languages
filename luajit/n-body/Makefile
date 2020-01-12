compile:

measure:
	/opt/rapl/main "${BINARY} nbody.lua-2.lua 50000000" Lua n-body

run:
	${BINARY} nbody.lua-2.lua 50000000

mem:
	/usr/bin/time -v  ${BINARY} nbody.lua-2.lua 50000000

valgrind:
	valgrind --tool=massif --stacks=yes  ${BINARY} nbody.lua-2.lua 50000000
