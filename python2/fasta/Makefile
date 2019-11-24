compile:
	echo "python2: nothing to compile"

measure:
	modprobe msr
	/opt/rapl/main "${BINARY} -OO fasta.python3-3.py 25000000" /opt/result/python2 fasta

run:
	${BINARY} -OO fasta.python3-3.py 25000000

make mem:
	/usr/bin/time -v  ${BINARY} -OO fasta.python3-3.py 25000000
