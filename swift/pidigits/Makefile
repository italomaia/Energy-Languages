compile:
	/usr/local/src/swift-2017-04-13-a-ubuntu16.10/usr/bin/swiftc pidigits.swift-2.swift -Ounchecked -whole-module-optimization -I Include/swift/gmp -o pidigits.swift-2.swift_run

xprepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./pidigits.swift-2.swift_run 10000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./pidigits.swift-2.swift_run 10000

