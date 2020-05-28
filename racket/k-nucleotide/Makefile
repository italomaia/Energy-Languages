compile:
	/usr/local/src/racket-6.8/bin/raco make knucleotide.racket-4.racket

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/local/src/racket-6.8/bin/racket ./compiled/knucleotide.racket-4_racket.zo 0 < /root/data/knucleotide-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/racket-6.8/bin/racket ./compiled/knucleotide.racket-4_racket.zo 0 < /root/data/knucleotide-input25000000.txt

