compile:

measure:
	/opt/rapl/main "php -n  spectralnorm.php 5500" PHP spectral-norm

run:
	php -n  spectralnorm.php 5500

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v php -n  spectralnorm.php 5500

valgrind:
	valgrind --tool=massif --stacks=yes php -n  spectralnorm.php 5500
