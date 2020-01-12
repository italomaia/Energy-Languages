compile:
	/usr/local/src/swift-2017-04-13-a-ubuntu16.10/usr/bin/swiftc fasta.swift-3.swift -Ounchecked -whole-module-optimization  -o fasta.swift-3.swift_run

run:
	./fasta.swift-3.swift_run 25000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./fasta.swift-3.swift_run 25000000

