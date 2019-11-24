compile:
	echo "python2: nothing to compile"

measure:
	modprobe msr
	/opt/rapl/main "${BINARY} -OO revcomp.python3-6.py 0 < /root/data/revcomp-input25000000.txt" /opt/result/python2 reverse-complement

run:
	${BINARY} -OO revcomp.python3-6.py 0 < /root/data/revcomp-input25000000.txt

mem:
	/usr/bin/time -v ${BINARY} -OO revcomp.python3-6.py 0 < /root/data/revcomp-input25000000.txt

