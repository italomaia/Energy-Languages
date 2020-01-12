compile:
	/usr/local/src/chapel-1.15.0/bin/linux64/chpl --fast fasta.chapel-2.chpl -o fasta.chapel-2.chapel_run
run:
	./fasta.chapel-2.chapel_run --n=25000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./fasta.chapel-2.chapel_run --n=25000000

