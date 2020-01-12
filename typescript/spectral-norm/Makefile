compile:
	cp spectralnorm.typescript spectralnorm.ts
	/usr/local/src/node-v7.9.0-linux-x64/bin/tsc --alwaysStrict -t ESNEXT  spectralnorm.ts

run:
	/usr/local/src/node-v7.9.0-linux-x64/bin/node --use_strict spectralnorm.js 5500

clean:
	rm -rf *.js *.ts

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/node-v7.9.0-linux-x64/bin/node --use_strict spectralnorm.js 5500


