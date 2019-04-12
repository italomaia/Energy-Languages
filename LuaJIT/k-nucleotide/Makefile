BINARY=/usr/bin/luajit

compile:

measure:
	sudo modprobe msr
	sudo ../../RAPL/main "${BINARY}  knucleotide.lua-2.lua 0 < knucleotide-input25000000.txt" Lua k-nucleotide

run:
	${BINARY}  knucleotide.lua-2.lua 0 < knucleotide-input25000000.txt

mem:
	/usr/bin/time -v ${BINARY}  knucleotide.lua-2.lua 0 < knucleotide-input25000000.txt

valgrind:
	valgrind --tool=massif --stacks=yes ${BINARY}  knucleotide.lua-2.lua 0 < knucleotide-input25000000.txt
