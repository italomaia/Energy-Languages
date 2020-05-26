compile:

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} regexredux.perl-4.perl 0 < /root/data/regexredux-input5000000.txt > /opt/results/${TEST_NAME}.${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} regexredux.perl-4.perl 0 < /root/data/regexredux-input5000000.txt
