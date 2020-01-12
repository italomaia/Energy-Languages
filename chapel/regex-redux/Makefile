compile:
	/usr/local/src/chapel-1.15.0/bin/linux64/chpl --fast regexredux.chpl -o regexredux.chapel_run
run:
	./regexredux.chapel_run --n=0 < /root/data/regexredux-input5000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./regexredux.chapel_run --n=0 < /root/data/regexredux-input5000000.txt

