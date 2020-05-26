compile:

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} binarytrees.perl-3.perl 21 > /opt/results/${TEST_NAME}.${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ${BINARY} binarytrees.perl-3.perl 21
