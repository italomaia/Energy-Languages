compile:

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	php -n  spectralnorm.php 5500

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v php -n  spectralnorm.php 5500

