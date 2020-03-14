compile:
	echo "nothing to do"

run:
	${BINARY} -OO binarytrees.py 21 >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -OO binarytrees.py 21
