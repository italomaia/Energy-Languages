compile:
	/usr/local/src/chapel-1.15.0/bin/linux64/chpl --fast revcomp.chpl -o revcomp.chapel_run
run:
	./revcomp.chapel_run --n=0 < /root/data/revcomp-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./revcomp.chapel_run --n=0 < /root/data/revcomp-input25000000.txt

