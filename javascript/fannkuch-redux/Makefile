compile:
	cp -L fannkuchredux.node-4.node fannkuchredux.node-4.js
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/local/src/node-v7.9.0-linux-x64/bin/node fannkuchredux.node-4.js 12

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/node-v7.9.0-linux-x64/bin/node fannkuchredux.node-4.js 12

