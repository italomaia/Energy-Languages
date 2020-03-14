compile:
	echo "python2: nothing to compile"

run:
	${BINARY} -OO knucleotide.py 0 < /root/data/knucleotide-input25000000.txt >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -OO knucleotide.py 0 < /root/data/knucleotide-input25000000.txt
