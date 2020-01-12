compile:

run:
	${BINARY} regexredux.perl-4.perl 0 < /root/data/regexredux-input5000000.txt >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} regexredux.perl-4.perl 0 < /root/data/regexredux-input5000000.txt
