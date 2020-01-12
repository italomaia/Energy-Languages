compile:
	cp mandelbrot.ghc-2.ghc mandelbrot.ghc-2.hs
	/usr/local/src/ghc-8.0.2/bin/ghc --make -fllvm -O2 -XBangPatterns -threaded -rtsopts  mandelbrot.ghc-2.hs -o mandelbrot.ghc-2.ghc_run
run:
	./mandelbrot.ghc-2.ghc_run +RTS -N4 -RTS 16000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./mandelbrot.ghc-2.ghc_run +RTS -N4 -RTS 16000

