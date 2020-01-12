compile:
	cp spectralnorm.python3-5.python3 spectralnorm.python3-5.py

run:
	${BINARY} -OO spectralnorm.python3-5.py 5500 >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -v ${BINARY} -OO spectralnorm.python3-5.py 5500
