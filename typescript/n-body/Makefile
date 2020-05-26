compile:
	cp nbody.typescript-3.typescript nbody.typescript-3.ts
	/usr/local/src/node-v7.9.0-linux-x64/bin/tsc --alwaysStrict -t ESNEXT  nbody.typescript-3.ts

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/local/src/node-v7.9.0-linux-x64/bin/node --use_strict nbody.typescript-3.js 50000000

clean:
	rm -rf *.js *.ts

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/node-v7.9.0-linux-x64/bin/node --use_strict nbody.typescript-3.js 50000000

