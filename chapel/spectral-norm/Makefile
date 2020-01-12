compile:
	/usr/local/src/chapel-1.15.0/bin/linux64/chpl --fast spectralnorm.chpl -o spectralnorm.chapel_run
run:
	./spectralnorm.chapel_run --n=5500

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./spectralnorm.chapel_run --n=5500

