compile:
	cp -L nbody.node nbody.js
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/local/src/node-v7.9.0-linux-x64/bin/node nbody.js 50000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  /usr/local/src/node-v7.9.0-linux-x64/bin/node nbody.js 50000000

