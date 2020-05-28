compile:
	/usr/local/src/swift-2017-04-13-a-ubuntu16.10/usr/bin/swiftc spectralnorm.swift-3.swift -Ounchecked -whole-module-optimization  -o spectralnorm.swift-3.swift_run

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./spectralnorm.swift-3.swift_run 5500

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./spectralnorm.swift-3.swift_run 5500


