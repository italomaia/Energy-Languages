BINARY=/usr/bin/ravi

compile:

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} revcomp.lua-2.lua 0 < /root/data/revcomp-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} revcomp.lua-2.lua 0 < /root/data/revcomp-input25000000.txt

