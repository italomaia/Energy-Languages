compile:
	/usr/local/src/chapel-1.15.0/bin/linux64/chpl --fast knucleotide.chpl -o knucleotide.chapel_run
run:
	./knucleotide.chapel_run --n=0 < /root/data/knucleotide-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./knucleotide.chapel_run --n=0 < /root/data/knucleotide-input25000000.txt



