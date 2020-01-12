compile:
	cp knucleotide.python3-3.python3 knucleotide.python3-3.py

run:
	${BINARY} -OO knucleotide.python3-3.py 0 < /root/data/knucleotide-input25000000.txt >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -v ${BINARY} -OO knucleotide.python3-3.py 0 < /root/data/knucleotide-input25000000.txt
