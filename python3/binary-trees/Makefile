compile:
	cp binarytrees.python3 binarytrees.py

run:
	${BINARY} -OO binarytrees.py 21 >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -v ${BINARY} -OO binarytrees.py 21 >> /opt/measures/${TLANG}.txt
