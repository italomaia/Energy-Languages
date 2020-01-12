compile:
	echo "luajit: nothing to do"

run:
	${BINARY} revcomp.lua-2.lua 0 < /root/data/revcomp-input25000000.txt >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -v ${BINARY} revcomp.lua-2.lua 0 < /root/data/revcomp-input25000000.txt >> /opt/measures/${TLANG}.txt
