compile:

measure:
	sudo modprobe msr
	sudo /opt/rapl/main "php -n  spectralnorm.php 5500" PHP spectral-norm

run:
	php -n  spectralnorm.php 5500

mem:
	/usr/bin/time -v php -n  spectralnorm.php 5500

valgrind:
	valgrind --tool=massif --stacks=yes php -n  spectralnorm.php 5500
