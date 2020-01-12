compile:
	echo "python2: nothing to compile"

run:
	${BINARY} -OO fannkuchredux.python3-4.py 12 >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -OO fannkuchredux.python3-4.py 12
