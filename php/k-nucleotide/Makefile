compile:

measure:
	/opt/rapl/main "php -d memory_limit=1024M knucleotide.php-4.php 0 < /root/data/knucleotide-input25000000.txt" PHP k-nucleotide

run:
	php -d memory_limit=1024M knucleotide.php-4.php 0 < /root/data/knucleotide-input25000000.txt

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v php -d memory_limit=1024M knucleotide.php-4.php 0 < /root/data/knucleotide-input25000000.txt

valgrind:
	valgrind --tool=massif --stacks=yes php -d memory_limit=1024M knucleotide.php-4.php 0 < /root/data/knucleotide-input25000000.txt
