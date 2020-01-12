compile:
	cp regexredux.typescript-3.typescript regexredux.typescript-3.ts
	/usr/local/src/node-v7.9.0-linux-x64/bin/tsc --alwaysStrict -t ESNEXT --lib es7 regexredux.typescript-3.ts

run:
	/usr/local/src/node-v7.9.0-linux-x64/bin/node --use_strict regexredux.typescript-3.js 0 < /root/data/regexredux-input5000000.txt

clean:
	rm -rf *.js *.ts

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/node-v7.9.0-linux-x64/bin/node --use_strict regexredux.typescript-3.js 0 < /root/data/regexredux-input5000000.txt

