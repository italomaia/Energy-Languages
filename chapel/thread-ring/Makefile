compile:
	/usr/local/src/chapel-1.15.0/bin/linux64/chpl --fast threadring.chpl -o threadring.chapel_run
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./threadring.chapel_run --n=50000000
