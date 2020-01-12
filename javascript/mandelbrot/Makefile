compile:
	cp -L mandelbrot.node mandelbrot.js
run:
	/usr/local/src/node-v7.9.0-linux-x64/bin/node mandelbrot.js 16000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/node-v7.9.0-linux-x64/bin/node mandelbrot.js 16000

