compile:
	/usr/local/src/chapel-1.15.0/bin/linux64/chpl --fast fannkuchredux.chpl -o fannkuchredux.chapel_run
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./fannkuchredux.chapel_run --n=12

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./fannkuchredux.chapel_run --n=12

