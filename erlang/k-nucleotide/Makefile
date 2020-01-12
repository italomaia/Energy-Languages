compile:
	cp knucleotide.hipe-3.hipe knucleotide.erl
	${COMPILER} +native +"{hipe, [o3]}" knucleotide.erl
measure:
	/opt/rapl/main "${BINARY} -smp enable -noshell -run  knucleotide main 0 < /root/data/knucleotide-input25000000.txt" Erlang k-nucleotide

run:
	${BINARY} -smp enable -noshell -run  knucleotide main 0 < /root/data/knucleotide-input25000000.txt

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -smp enable -noshell -run  knucleotide main 0 < /root/data/knucleotide-input25000000.txt

valgrind:
	valgrind --tool=massif --stacks=yes ${BINARY} -smp enable -noshell -run  knucleotide main 0 < /root/data/knucleotide-input25000000.txt
