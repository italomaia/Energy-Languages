compile:
	/usr/local/src/chapel-1.15.0/bin/linux64/chpl --fast spectralnorm.chpl -o spectralnorm.chapel_run
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./spectralnorm.chapel_run --n=5500

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./spectralnorm.chapel_run --n=5500

