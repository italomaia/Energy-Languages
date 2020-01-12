compile:
	echo "python2: nothing to compile"

run:
	${BINARY} -OO regexredux.py 0 < /root/data/regexredux-input5000000.txt

measure:
	/usr/bin/time -v ${BINARY} -OO regexredux.py 0 < /root/data/regexredux-input5000000.txt >> >> /opt/result/${TLANG}.txt
