compile:
	/usr/local/src/chapel-1.15.0/bin/linux64/chpl --fast binarytrees.chpl -o binarytrees.chapel_run
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./binarytrees.chapel_run --n=21

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./binarytrees.chapel_run --n=21

