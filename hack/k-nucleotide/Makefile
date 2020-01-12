compile:
	/usr/bin/hh_client

run:
	/usr/bin/hhvm  knucleotide.hack-4.hack 0 < /root/data/knucleotide-input25000000.txt
	killall hh_server

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  /usr/bin/hhvm  knucleotide.hack-4.hack 0 < /root/data/knucleotide-input25000000.txt
	 killall hh_server

	killall hh_server
