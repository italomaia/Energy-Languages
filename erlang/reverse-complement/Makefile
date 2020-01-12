compile:
	cp revcomp.hipe revcomp.erl
	${COMPILER} +native +"{hipe, [o3]}" revcomp.erl
run:
	${BINARY} -smp enable -noshell -run  revcomp main 0 < /root/data/revcomp-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -smp enable -noshell -run  revcomp main 0 < /root/data/revcomp-input25000000.txt

