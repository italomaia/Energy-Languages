compile:

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	php -n -d memory_limit=4096M binarytrees.php-5.php 21

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v php -n -d memory_limit=4096M binarytrees.php-5.php 21

