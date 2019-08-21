BINARY=/usr/bin/lua5.1

compile:

measure:
	sudo modprobe msr
	sudo /opt/rapl/main "${BINARY}  spectralnorm.lua 5500" Lua spectral-norm

run:
	${BINARY}  spectralnorm.lua 5500

mem:
	/usr/bin/time -v ${BINARY}  spectralnorm.lua 5500

valgrind:
	valgrind --tool=massif --stacks=yes ${BINARY}  spectralnorm.lua 5500
