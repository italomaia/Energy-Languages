compile:
	echo "lua53: nothing to do"

run:
	${BINARY} revcomp.lua-2.lua 0 < /root/data/revcomp-input25000000.txt >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} revcomp.lua-2.lua 0 < /root/data/revcomp-input25000000.txt
