compile:
	/usr/bin/hh_client

measure:
	/opt/rapl/main "/usr/bin/hhvm  mandelbrot.hack-3.hack 16000" Hack mandelbrot

run:
	/usr/bin/hhvm  mandelbrot.hack-3.hack 16000
	killall hh_server

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/bin/hhvm  mandelbrot.hack-3.hack 16000
	killall hh_server

valgrind:
	valgrind --tool=massif --stacks=yes /usr/bin/hhvm  mandelbrot.hack-3.hack 16000
	killall hh_server
