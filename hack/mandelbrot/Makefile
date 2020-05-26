compile:
	/usr/bin/hh_client

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/bin/hhvm  mandelbrot.hack-3.hack 16000
	killall hh_server

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/bin/hhvm  mandelbrot.hack-3.hack 16000
	killall hh_server

	killall hh_server
