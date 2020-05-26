compile:

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	php -n -d memory_limit=1024M revcomp.php-3.php 0 < /root/data/revcomp-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v php -n -d memory_limit=1024M revcomp.php-3.php 0 < /root/data/revcomp-input25000000.txt




