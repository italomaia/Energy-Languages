compile:
	echo "python2: nothing to compile"

run:
	${BINARY} -OO nbody.py 50000000 >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -OO nbody.py 50000000
