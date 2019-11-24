BINARY=/usr/bin/ravi

compile:

measure:
	sudo /opt/rapl/main "${BINARY}  fasta.lua-3.lua 25000000" Lua fasta

run:
	${BINARY}  fasta.lua-3.lua 25000000

mem:
	/usr/bin/time -v  ${BINARY}  fasta.lua-3.lua 25000000

valgrind:
	valgrind --tool=massif --stacks=yes  ${BINARY}  fasta.lua-3.lua 25000000
