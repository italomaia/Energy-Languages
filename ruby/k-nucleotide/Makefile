compile:


measure:
	/opt/rapl/main "${BINARY} -W0 knucleotide.yarv-7.yarv 0 < /root/data/knucleotide-input25000000.txt" Ruby k-nucleotide

run:
	${BINARY} -W0 knucleotide.yarv-7.yarv 0 < /root/data/knucleotide-input25000000.txt

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -W0 knucleotide.yarv-7.yarv 0 < /root/data/knucleotide-input25000000.txt

valgrind:
	valgrind --tool=massif --stacks=yes ${BINARY} -W0 knucleotide.yarv-7.yarv 0 < /root/data/knucleotide-input25000000.txt
