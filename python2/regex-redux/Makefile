compile:
	cp regexredux.python3 regexredux.py
measure:
	sudo modprobe msr
	sudo /opt/rapl/main "${BINARY} -OO regexredux.py 0 < /root/data/regexredux-input5000000.txt" Python regex-redux

run:
	${BINARY} -OO regexredux.py 0 < /root/data/regexredux-input5000000.txt

mem:
	/usr/bin/time -v ${BINARY} -OO regexredux.py 0 < /root/data/regexredux-input5000000.txt
