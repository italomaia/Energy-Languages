compile:
	cp fasta.python3-3.python3 fasta.python3-3.py
measure:
	sudo /opt/rapl/main "${BINARY} -OO fasta.python3-3.py 25000000" Python fasta

run:
	${BINARY} -OO fasta.python3-3.py 25000000

make mem:
	/usr/bin/time -v  ${BINARY} -OO fasta.python3-3.py 25000000
