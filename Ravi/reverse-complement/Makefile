BINARY=/usr/bin/ravi

compile:

measure:
	sudo modprobe msr
	sudo ../../RAPL/main "${BINARY}  revcomp.lua-2.lua 0 < ../../revcomp-input25000000.txt" Lua reverse-complement

run:
	${BINARY}  revcomp.lua-2.lua 0 < ../../revcomp-input25000000.txt

mem:
	/usr/bin/time -v ${BINARY}  revcomp.lua-2.lua 0 < ../../revcomp-input25000000.txt

valgrind:
	valgrind --tool=massif --stacks=yes ${BINARY}  revcomp.lua-2.lua 0 < ../../revcomp-input25000000.txt
