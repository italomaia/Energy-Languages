compile:
	echo "python2: nothing to compile"

measure:
	modprobe msr
	/opt/rapl/main "${BINARY} -OO pidigits.python3-2.py 10000" /opt/result/python2 pidigits

run:
	${BINARY} -OO pidigits.python3-2.py 10000
mem:
	/usr/bin/time -v ${BINARY} -OO pidigits.python3-2.py 10000
