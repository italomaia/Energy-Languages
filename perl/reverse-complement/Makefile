compile:

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} revcomp.perl-3.perl 0 < /root/data/revcomp-input25000000.txt > /opt/results/${TEST_NAME}.${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} revcomp.perl-3.perl 0 < /root/data/revcomp-input25000000.txt
