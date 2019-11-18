BINARY=/usr/bin/lua5.1

compile:

xmeasure:
	sudo modprobe msr
	sudo /opt/rapl/main "${BINARY}  pidigits.lua-5.lua 10000" Lua pidigits

run:
	${BINARY}  pidigits.lua-5.lua 10000

mem:
	/usr/bin/time -v ${BINARY}  pidigits.lua-5.lua 10000


valgrind:
	valgrind --tool=massif --stacks=yes ${BINARY}  pidigits.lua-5.lua 10000

