BINARY=/usr/bin/ravi

compile:

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} fasta.lua-3.lua 25000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ${BINARY} fasta.lua-3.lua 25000000

