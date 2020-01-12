compile:
	echo "lua53: nothing to do"

run:
	${BINARY} fasta.lua-3.lua 25000000 >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ${BINARY} fasta.lua-3.lua 25000000
