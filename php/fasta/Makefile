compile:

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	php -n  fasta.php-3.php 25000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v php -n  fasta.php-3.php 25000000

