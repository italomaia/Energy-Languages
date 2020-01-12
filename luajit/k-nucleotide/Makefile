compile:
	echo "luajit: nothing to do"

run:
	${BINARY} knucleotide.lua-2.lua 0 < /root/data/knucleotide-input25000000.txt >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} knucleotide.lua-2.lua 0 < /root/data/knucleotide-input25000000.txt
