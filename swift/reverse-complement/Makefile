compile:
	/usr/local/src/swift-2017-04-13-a-ubuntu16.10/usr/bin/swiftc revcomp.swift -Ounchecked -whole-module-optimization  -o revcomp.swift_run

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./revcomp.swift_run 0 < /root/data/revcomp-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./revcomp.swift_run 0 < /root/data/revcomp-input25000000.txt

