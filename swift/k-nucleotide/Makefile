compile:
	/usr/local/src/swift-2017-04-13-a-ubuntu16.10/usr/bin/swiftc knucleotide.swift-2.swift -Ounchecked -whole-module-optimization  -o knucleotide.swift-2.swift_run

measure:
	/opt/rapl/main "./knucleotide.swift-2.swift_run 0 < /root/data/knucleotide-input25000000.txt" Swift k-nucleotide

run:
	./knucleotide.swift-2.swift_run 0 < /root/data/knucleotide-input25000000.txt

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./knucleotide.swift-2.swift_run 0 < /root/data/knucleotide-input25000000.txt

valgrind:
	valgrind --tool=massif --stacks=yes ./knucleotide.swift-2.swift_run 0 < /root/data/knucleotide-input25000000.txt
