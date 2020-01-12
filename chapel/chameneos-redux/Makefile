compile:
	/usr/local/src/chapel-1.15.0/bin/linux64/chpl --fast chameneosredux.chpl -o chameneosredux.chapel_run
run:
	./chameneosredux.chapel_run --n=6000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./chameneosredux.chapel_run --n=6000000

