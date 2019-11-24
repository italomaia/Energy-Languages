compile:
	echo "python2: nothing to compile"

measure:
	modprobe msr
	/opt/rapl/main "${BINARY} -OO nbody.py 50000000" /opt/result/python2 n-body

run:
	${BINARY} -OO nbody.py 50000000

mem:
	/usr/bin/time -v ${BINARY} -OO nbody.py 50000000
