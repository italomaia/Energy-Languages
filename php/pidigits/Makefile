compile:

xmeasure:
	/opt/rapl/main "php -n  pidigits.php-5.php 10000" PHP pidigits

run:
	php -n  pidigits.php-5.php 10000

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v php -n  pidigits.php-5.php 10000

valgrind:
	valgrind --tool=massif --stacks=yes php -n  pidigits.php-5.php 10000
