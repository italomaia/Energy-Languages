compile:
	/usr/local/src/swift-2017-04-13-a-ubuntu16.10/usr/bin/swiftc knucleotide.swift-2.swift -Ounchecked -whole-module-optimization  -o knucleotide.swift-2.swift_run

run:
	./knucleotide.swift-2.swift_run 0 < /root/data/knucleotide-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./knucleotide.swift-2.swift_run 0 < /root/data/knucleotide-input25000000.txt

