compile:

run:
	${BINARY} knucleotide.perl 0 < /root/data/knucleotide-input25000000.txt > /opt/results/${TEST_NAME}.${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} knucleotide.perl 0 < /root/data/knucleotide-input25000000.txt
