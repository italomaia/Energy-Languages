compile:
	echo "python2: nothing to compile"

measure:
	modprobe msr
	/opt/rapl/main "${BINARY} -OO fannkuchredux.python3-4.py 12" /opt/result/python2 fannkuch-redux

run:
	${BINARY} -OO fannkuchredux.python3-4.py 12
mem:
	/usr/bin/time -v ${BINARY} -OO fannkuchredux.python3-4.py 12
