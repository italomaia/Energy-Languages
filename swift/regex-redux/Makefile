compile:
	/usr/local/src/swift-2017-04-13-a-ubuntu16.10/usr/bin/swiftc regexredux.swift-2.swift -Ounchecked -whole-module-optimization  -o regexredux.swift-2.swift_run

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./regexredux.swift-2.swift_run 0 < /root/data/regexredux-input5000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./regexredux.swift-2.swift_run 0 < /root/data/regexredux-input5000000.txt

