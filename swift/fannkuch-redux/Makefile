compile:
	/usr/local/src/swift-2017-04-13-a-ubuntu16.10/usr/bin/swiftc fannkuchredux.swift-3.swift -Ounchecked -whole-module-optimization  -o fannkuchredux.swift-3.swift_run

run:
	./fannkuchredux.swift-3.swift_run 12

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./fannkuchredux.swift-3.swift_run 12

