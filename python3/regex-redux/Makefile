compile:
	cp regexredux.python3 regexredux.py

run:
	${BINARY} -OO regexredux.py 0 < /root/data/regexredux-input5000000.txt >> /opt/results/${TLANG}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} -OO regexredux.py 0 < /root/data/regexredux-input5000000.txt
