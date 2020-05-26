compile:

xprepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	php -n  pidigits.php-5.php 10000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v php -n  pidigits.php-5.php 10000

