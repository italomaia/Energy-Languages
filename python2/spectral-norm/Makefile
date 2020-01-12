compile:
	echo "python2: nothing to compile"

run:
	${BINARY} -OO spectralnorm.python3-5.py 5500 >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -OO spectralnorm.python3-5.py 5500
