compile:
	echo "python2: nothing to compile"

measure:
	modprobe msr
	/opt/rapl/main "${BINARY} -OO knucleotide.python3-3.py 0 < /root/data/knucleotide-input25000000.txt" /opt/result/python2 k-nucleotide

run:
	${BINARY} -OO knucleotide.python3-3.py 0 < /root/data/knucleotide-input25000000.txt

mem:
	/usr/bin/time -v ${BINARY} -OO knucleotide.python3-3.py 0 < /root/data/knucleotide-input25000000.txt
