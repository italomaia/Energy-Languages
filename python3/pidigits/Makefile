compile:
	cp pidigits.python3-2.python3 pidigits.python3-2.py
measure:
	sudo /opt/rapl/main "${BINARY} -OO pidigits.python3-2.py 10000" Python pidigits

run:
	${BINARY} -OO pidigits.python3-2.py 10000
mem:
	/usr/bin/time -v ${BINARY} -OO pidigits.python3-2.py 10000
