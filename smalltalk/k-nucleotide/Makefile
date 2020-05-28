compile:


prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/local/src/vw8.1.1pul/bin/linuxx86_64/vwlinuxx86_64 /usr/local/src/vw8.1.1pul/image/benchmarks.im -nogui -evaluate \"Tests knucleotide5\" -a 0 < /root/data/knucleotide-input25000000.txt
