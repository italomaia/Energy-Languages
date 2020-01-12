compile:

measure:
	/opt/rapl/main "php  fannkuchredux.php-3.php 12" PHP fannkuch-redux

run:
	php  fannkuchredux.php-3.php 12

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v php  fannkuchredux.php-3.php 12

valgrind:
	valgrind --tool=massif --stacks=yes php  fannkuchredux.php-3.php 12
