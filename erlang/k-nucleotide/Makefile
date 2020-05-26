compile:
	cp knucleotide.hipe-3.hipe knucleotide.erl
	${COMPILER} +native +"{hipe, [o3]}" knucleotide.erl
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} -smp enable -noshell -run  knucleotide main 0 < /root/data/knucleotide-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -smp enable -noshell -run  knucleotide main 0 < /root/data/knucleotide-input25000000.txt

