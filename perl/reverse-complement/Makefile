compile:

measure:
	sudo modprobe msr
	sudo /opt/rapl/main "${BINARY} revcomp.perl-3.perl 0 < /root/data/revcomp-input25000000.txt" Perl reverse-complement

run:
	${BINARY} revcomp.perl-3.perl 0 < /root/data/revcomp-input25000000.txt

mem:
	/usr/bin/time -v ${BINARY} revcomp.perl-3.perl 0 < /root/data/revcomp-input25000000.txt

valgrind:
	valgrind --tool=massif --stacks=yes ${BINARY} revcomp.perl-3.perl 0 < /root/data/revcomp-input25000000.txt
