compile:
	cp fannkuchredux.python3-4.python3 fannkuchredux.python3-4.py
measure:
	sudo /opt/rapl/main "${BINARY} -OO fannkuchredux.python3-4.py 12" Python fannkuch-redux

run:
	${BINARY} -OO fannkuchredux.python3-4.py 12
mem:
	/usr/bin/time -v ${BINARY} -OO fannkuchredux.python3-4.py 12
