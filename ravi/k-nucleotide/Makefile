BINARY=/usr/bin/ravi

compile:

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} knucleotide.lua-2.lua 0 < /root/data/knucleotide-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} knucleotide.lua-2.lua 0 < /root/data/knucleotide-input25000000.txt

