compile:
	/usr/bin/hh_client

measure:
	/opt/rapl/main "/usr/bin/hhvm  fannkuchredux.hack-3.hack 12" Hack fannkuch-redux

run:
	/usr/bin/hhvm  fannkuchredux.hack-3.hack 12
	killall hh_server
mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/bin/hhvm  fannkuchredux.hack-3.hack 12
	killall hh_server

valgrind:
	valgrind --tool=massif --stacks=yes /usr/bin/hhvm  fannkuchredux.hack-3.hack 12
	 killall hh_server
