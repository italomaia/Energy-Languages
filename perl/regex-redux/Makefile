compile:

measure:
	sudo modprobe msr
	sudo /opt/rapl/main "${BINARY} regexredux.perl-4.perl 0 < /root/data/regexredux-input5000000.txt" Perl regex-redux

run:
	${BINARY} regexredux.perl-4.perl 0 < /root/data/regexredux-input5000000.txt

mem:
	/usr/bin/time -v ${BINARY} regexredux.perl-4.perl 0 < /root/data/regexredux-input5000000.txt

valgrind:
	valgrind --tool=massif --stacks=yes ${BINARY} regexredux.perl-4.perl 0 < /root/data/regexredux-input5000000.txt
