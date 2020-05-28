compile:
	/usr/local/src/swift-2017-04-13-a-ubuntu16.10/usr/bin/swiftc mandelbrot.swift-3.swift -Ounchecked -whole-module-optimization  -o mandelbrot.swift-3.swift_run

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./mandelbrot.swift-3.swift_run 16000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./mandelbrot.swift-3.swift_run 16000

