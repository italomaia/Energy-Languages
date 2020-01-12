compile:
	cp nbody.python3 nbody.py

run:
	${BINARY} -OO nbody.py 50000000 >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -v ${BINARY} -OO nbody.py 50000000 >> /opt/measures/${TLANG}.txt
