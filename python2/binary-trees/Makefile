compile:
	echo "python2: nothing to compile"

run:
	${BINARY} -OO binarytrees.py 21 >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -OO binarytrees.py 21
