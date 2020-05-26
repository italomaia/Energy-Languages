compile:
	cp -L spectralnorm.node-2.node spectralnorm.node-2.js
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/local/src/node-v7.9.0-linux-x64/bin/node spectralnorm.node-2.js 5500

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/node-v7.9.0-linux-x64/bin/node spectralnorm.node-2.js 5500

