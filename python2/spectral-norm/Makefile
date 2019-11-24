compile:
	echo "python2: nothing to compile"

measure:
	modprobe msr
	/opt/rapl/main "${BINARY} -OO spectralnorm.python3-5.py 5500" /opt/result/python2 spectral-norm

run:
	${BINARY} -OO spectralnorm.python3-5.py 5500

mem:
	/usr/bin/time -v ${BINARY} -OO spectralnorm.python3-5.py 5500
