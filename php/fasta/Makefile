compile:

measure:
	/opt/rapl/main "php -n  fasta.php-3.php 25000000" PHP fasta

run:
	php -n  fasta.php-3.php 25000000

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v php -n  fasta.php-3.php 25000000

valgrind:
	valgrind --tool=massif --stacks=yes php -n  fasta.php-3.php 25000000
