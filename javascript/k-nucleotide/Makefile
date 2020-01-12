compile:
	cp -L knucleotide.node-2.node knucleotide.node-2.js
run:
	/usr/local/src/node-v7.9.0-linux-x64/bin/node knucleotide.node-2.js 0 < /root/data/knucleotide-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/node-v7.9.0-linux-x64/bin/node knucleotide.node-2.js 0 < /root/data/knucleotide-input25000000.txt

