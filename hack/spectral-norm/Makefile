compile:
	/usr/bin/hh_client

run:
	/usr/bin/hhvm  spectralnorm.hack-3.hack 5500
	killall hh_server

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/bin/hhvm  spectralnorm.hack-3.hack 5500
	killall hh_server

	killall hh_server
