compile:
	cp revcomp.python3-6.python3 revcomp.python3-6.py
measure:
	sudo /opt/rapl/main "${BINARY} -OO revcomp.python3-6.py 0 < /root/data/revcomp-input25000000.txt" Python reverse-complement

run:
	${BINARY} -OO revcomp.python3-6.py 0 < /root/data/revcomp-input25000000.txt

mem:
	/usr/bin/time -v ${BINARY} -OO revcomp.python3-6.py 0 < /root/data/revcomp-input25000000.txt

