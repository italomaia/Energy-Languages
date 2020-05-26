compile:
	/usr/local/src/chapel-1.15.0/bin/linux64/chpl --fast nbody.chpl -o nbody.chapel_run
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./nbody.chapel_run --n=50000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./nbody.chapel_run --n=50000000

