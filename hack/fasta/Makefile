compile:
	/usr/bin/hh_client

run:
	/usr/bin/hhvm  fasta.hack-4.hack 25000000
	killall hh_server

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/bin/hhvm  fasta.hack-4.hack 25000000
	killall hh_server

	killall hh_server
