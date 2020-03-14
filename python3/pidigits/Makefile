compile:
	echo "nothing to do"

run:
	${BINARY} -OO pidigits.py 10000 >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -OO pidigits.py 10000
