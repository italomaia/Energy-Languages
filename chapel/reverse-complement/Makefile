compile:
	/usr/local/src/chapel-1.15.0/bin/linux64/chpl --fast revcomp.chpl -o revcomp.chapel_run
measure:
	/opt/rapl/main "./revcomp.chapel_run --n=0 < /root/data/revcomp-input25000000.txt" Chapel reverse-complement

run:
	./revcomp.chapel_run --n=0 < /root/data/revcomp-input25000000.txt

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./revcomp.chapel_run --n=0 < /root/data/revcomp-input25000000.txt

valgrind:
	valgrind --tool=massif --stacks=yes ./revcomp.chapel_run --n=0 < /root/data/revcomp-input25000000.txt
