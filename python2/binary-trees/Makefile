compile:
	cp binarytrees.python3 binarytrees.py

measure:
	sudo modprobe msr
	sudo /opt/rapl/main "/usr/bin/python -OO binarytrees.py 21" Python binary-trees

run:
	/usr/bin/python -OO binarytrees.py 21

mem:
	/usr/bin/time -v /usr/bin/python -OO binarytrees.py 21
