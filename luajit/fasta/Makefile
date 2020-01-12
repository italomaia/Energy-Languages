compile:
	echo "luajit: nothing to do"

run:
	${BINARY} fasta.lua-3.lua 25000000 >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -v  ${BINARY} fasta.lua-3.lua 25000000 >> /opt/measures/${TLANG}.txt
