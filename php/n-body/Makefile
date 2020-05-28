compile:

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	php -n  nbody.php-3.php 50000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  php -n  nbody.php-3.php 50000000

