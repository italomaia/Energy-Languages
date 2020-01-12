compile:
	echo "python2: nothing to compile"

run:
	${BINARY} -OO knucleotide.python3-3.py 0 < /root/data/knucleotide-input25000000.txt

measure:
	/usr/bin/time -v ${BINARY} -OO knucleotide.python3-3.py 0 < /root/data/knucleotide-input25000000.txt >> /opt/result/${TLANG}.txt
