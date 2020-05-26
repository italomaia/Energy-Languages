compile:
	echo "lua53: nothing to do"

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} revcomp.lua-2.lua 0 < /root/data/revcomp-input25000000.txt > /opt/results/${TEST_NAME}.${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} revcomp.lua-2.lua 0 < /root/data/revcomp-input25000000.txt
