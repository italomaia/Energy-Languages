compile:
	/usr/bin/hh_client

xprepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/bin/hhvm  nbody.hack-5.hack 50000000
	killall hh_server

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/bin/hhvm  nbody.hack-5.hack 50000000
	killall hh_server

	killall hh_server
