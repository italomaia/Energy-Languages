BINARY=/usr/bin/lua5.3

compile:

xmeasure:
	sudo modprobe msr
	sudo /opt/rapl/main "${BINARY}  regexredux.lua-2.lua 0 < ../../regexredux-input50000.txt" Lua regex-redux

run:
	${BINARY}  regexredux.lua-2.lua 0 < ../../regexredux-input50000.txt

mem:
	/usr/bin/time -v ${BINARY}  regexredux.lua-2.lua 0 < ../../regexredux-input50000.txt

valgrind:
	valgrind --tool=massif --stacks=yes ${BINARY}  regexredux.lua-2.lua 0 < ../../regexredux-input50000.txt
