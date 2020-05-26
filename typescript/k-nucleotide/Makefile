compile:
	cp knucleotide.typescript knucleotide.ts
	/usr/local/src/node-v7.9.0-linux-x64/bin/tsc --alwaysStrict -t ESNEXT  knucleotide.ts
	/usr/local/src/node-v7.9.0-linux-x64/lib/node_modules/babel-cli/bin/babel.js --plugins transform-es2015-modules-commonjs knucleotide.js -o knucleotide.js

xprepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/local/src/node-v7.9.0-linux-x64/bin/node --use_strict knucleotide.js 0 < /root/data/knucleotide-input25000000.txt

clean:
	rm -rf *.js *.ts

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/node-v7.9.0-linux-x64/bin/node --use_strict knucleotide.js 0 < /root/data/knucleotide-input25000000.txt

