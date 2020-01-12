compile:
	cp binarytrees.typescript-2.typescript binarytrees.typescript-2.ts
	/usr/local/src/node-v7.9.0-linux-x64/bin/tsc --alwaysStrict -t ESNEXT  binarytrees.typescript-2.ts

run:
	/usr/local/src/node-v7.9.0-linux-x64/bin/node --use_strict binarytrees.typescript-2.js 21

clean:
	rm -rf *.js *.ts

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/node-v7.9.0-linux-x64/bin/node --use_strict binarytrees.typescript-2.js 21


