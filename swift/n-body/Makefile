compile:
	/usr/local/src/swift-2017-04-13-a-ubuntu16.10/usr/bin/swiftc nbody.swift-5.swift -Ounchecked -whole-module-optimization  -o nbody.swift-5.swift_run

measure:
	/opt/rapl/main "./nbody.swift-5.swift_run 50000000" Swift n-body

run:
	./nbody.swift-5.swift_run 50000000

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./nbody.swift-5.swift_run 50000000

valgrind:
	valgrind --tool=massif --stacks=yes  ./nbody.swift-5.swift_run 50000000
