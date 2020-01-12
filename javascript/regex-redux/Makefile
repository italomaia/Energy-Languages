compile:
	cp -L regexredux.node-2.node regexredux.node-2.js
run:
	/usr/local/src/node-v7.9.0-linux-x64/bin/node regexredux.node-2.js 0 < /root/data/regexredux-input5000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/node-v7.9.0-linux-x64/bin/node regexredux.node-2.js 0 < /root/data/regexredux-input5000000.txt

