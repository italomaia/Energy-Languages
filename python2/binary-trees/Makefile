compile:
	cp binarytrees.python3 binarytrees.py

measure:
	sudo modprobe msr
	sudo /opt/rapl/main "${BINARY} -OO binarytrees.py 21" Python binary-trees

run:
	${BINARY} -OO binarytrees.py 21

mem:
	/usr/bin/time -v ${BINARY} -OO binarytrees.py 21
