compile:
	/usr/bin/hh_client

measure:
	/opt/rapl/main "/usr/bin/hhvm  spectralnorm.hack-3.hack 5500" Hack spectral-norm

run:
	/usr/bin/hhvm  spectralnorm.hack-3.hack 5500
	killall hh_server

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/bin/hhvm  spectralnorm.hack-3.hack 5500
	killall hh_server

valgrind:
	valgrind --tool=massif --stacks=yes /usr/bin/hhvm  spectralnorm.hack-3.hack 5500
	killall hh_server
