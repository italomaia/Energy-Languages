compile:
	cp fasta.hipe-2.hipe fasta.erl
	${COMPILER} +native +"{hipe, [o3]}" fasta.erl
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} -smp enable -noshell -run  fasta main 25000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -smp enable -noshell -run  fasta main 25000000
