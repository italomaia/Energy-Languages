BINARY=/usr/bin/ravi

compile:

measure:
	/opt/rapl/main "${BINARY} revcomp.lua-2.lua 0 < /root/data/revcomp-input25000000.txt" Lua reverse-complement

run:
	${BINARY} revcomp.lua-2.lua 0 < /root/data/revcomp-input25000000.txt

mem:
	/usr/bin/time -v ${BINARY} revcomp.lua-2.lua 0 < /root/data/revcomp-input25000000.txt

valgrind:
	valgrind --tool=massif --stacks=yes ${BINARY} revcomp.lua-2.lua 0 < /root/data/revcomp-input25000000.txt
