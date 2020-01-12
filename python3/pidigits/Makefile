compile:
	cp pidigits.python3-2.python3 pidigits.python3-2.py

run:
	${BINARY} -OO pidigits.python3-2.py 10000 >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -OO pidigits.python3-2.py 10000
