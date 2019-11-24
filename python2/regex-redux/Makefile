compile:
	echo "python2: nothing to compile"

measure:
	modprobe msr
	/opt/rapl/main "${BINARY} -OO regexredux.py 0 < /root/data/regexredux-input5000000.txt" /opt/result/python2 regex-redux

run:
	${BINARY} -OO regexredux.py 0 < /root/data/regexredux-input5000000.txt

mem:
	/usr/bin/time -v ${BINARY} -OO regexredux.py 0 < /root/data/regexredux-input5000000.txt
