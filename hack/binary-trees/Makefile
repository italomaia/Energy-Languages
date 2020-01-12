compile:
	/usr/bin/hh_client

measure:
	/opt/rapl/main "/usr/bin/hhvm  binarytrees.hack-4.hack 21" Hack binary-trees

run:
	/usr/bin/hhvm binarytrees.hack-4.hack 21
	killall hh_server

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/bin/hhvm binarytrees.hack-4.hack 21
	killall hh_server

valgrind:
	valgrind --tool=massif --stacks=yes /usr/bin/hhvm binarytrees.hack-4.hack 21
	killall hh_server
