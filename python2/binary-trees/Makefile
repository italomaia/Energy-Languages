compile:
	echo "python2: nothing to compile"

measure:
	modprobe msr
	/opt/rapl/main "${BINARY} -OO binarytrees.py 21" /opt/result/python2 binary-trees

run:
	${BINARY} -OO binarytrees.py 21

mem:
	/usr/bin/time -v ${BINARY} -OO binarytrees.py 21
