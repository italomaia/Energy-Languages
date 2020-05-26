compile:
	cp -L revcomp.node-7.node revcomp.node-7.js
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/local/src/node-v7.9.0-linux-x64/bin/node revcomp.node-7.js 0 < /root/data/revcomp-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/node-v7.9.0-linux-x64/bin/node revcomp.node-7.js 0 < /root/data/revcomp-input25000000.txt

