compile:
	cp fannkuchredux.typescript fannkuchredux.ts
	/usr/local/src/node-v7.9.0-linux-x64/bin/tsc --alwaysStrict -t ESNEXT  fannkuchredux.ts

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/local/src/node-v7.9.0-linux-x64/bin/node --use_strict fannkuchredux.js 12

clean:
	rm -rf *.js *.ts

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/node-v7.9.0-linux-x64/bin/node --use_strict fannkuchredux.js 12

