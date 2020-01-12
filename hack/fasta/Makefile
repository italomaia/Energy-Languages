compile:
	/usr/bin/hh_client

measure:
	/opt/rapl/main "/usr/bin/hhvm  fasta.hack-4.hack 25000000" Hack fasta

run:
	/usr/bin/hhvm  fasta.hack-4.hack 25000000
	killall hh_server

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/bin/hhvm  fasta.hack-4.hack 25000000
	killall hh_server

valgrind:
	valgrind --tool=massif --stacks=yes /usr/bin/hhvm  fasta.hack-4.hack 25000000
	killall hh_server
