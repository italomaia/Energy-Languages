compile:

measure:
	sudo modprobe msr
	sudo /opt/rapl/main "${BINARY} spectralnorm.perl-4.perl 5500" Perl spectral-norm

run:
	${BINARY} spectralnorm.perl-4.perl 5500

mem:
	/usr/bin/time -v  ${BINARY} spectralnorm.perl-4.perl 5500

valgrind:
	valgrind --tool=massif --stacks=yes  ${BINARY} spectralnorm.perl-4.perl 5500
