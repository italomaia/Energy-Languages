compile:
	/usr/local/src/swift-2017-04-13-a-ubuntu16.10/usr/bin/swiftc nbody.swift-5.swift -Ounchecked -whole-module-optimization  -o nbody.swift-5.swift_run

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./nbody.swift-5.swift_run 50000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./nbody.swift-5.swift_run 50000000

