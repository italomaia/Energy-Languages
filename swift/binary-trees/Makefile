compile:
	/usr/local/src/swift-2017-04-13-a-ubuntu16.10/usr/bin/swiftc binarytrees.swift-9.swift -Ounchecked -whole-module-optimization -I Include/swift/apr -o binarytrees.swift-9.swift_run

xrun:
	./binarytrees.swift-9.swift_run 21

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./binarytrees.swift-9.swift_run 21

