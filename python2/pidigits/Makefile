compile:
	echo "python2: nothing to compile"

run:
	${BINARY} -OO pidigits.python3-2.py 10000 >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -v ${BINARY} -OO pidigits.python3-2.py 10000 >> /opt/measures/${TLANG}.txt
