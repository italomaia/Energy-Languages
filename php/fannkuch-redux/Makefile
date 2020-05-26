compile:

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	php  fannkuchredux.php-3.php 12

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v php  fannkuchredux.php-3.php 12

