compile:
	cp binarytrees.python3 binarytrees.py

measure:
	sudo modprobe msr
	sudo /opt/rapl/main "${BINARY} -OO binarytrees.py 21" /opt/result/python2 binary-trees

run:
	${BINARY} -OO binarytrees.py 21

mem:
	/usr/bin/time -v ${BINARY} -OO binarytrees.py 21
