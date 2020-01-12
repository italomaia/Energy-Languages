compile:
	echo "python2: nothing to compile"

run:
	${BINARY} -OO nbody.py 50000000

measure:
	/usr/bin/time -v ${BINARY} -OO nbody.py 50000000 >> >> /opt/result/${TLANG}.txt
