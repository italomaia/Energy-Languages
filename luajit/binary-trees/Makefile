compile:

measure:
	/opt/rapl/main "${BINARY}  binarytrees.lua-2.lua 21" Lua binary-trees

run:
	${BINARY}  binarytrees.lua-2.lua 21

mem:
	/usr/bin/time -v ${BINARY}  binarytrees.lua-2.lua 21

valgrind:
	valgrind --tool=massif --stacks=yes ${BINARY}  binarytrees.lua-2.lua 21
