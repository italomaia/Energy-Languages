compile:
	cp fannkuchredux.ghc-3.ghc fannkuchredux.ghc-3.hs
	/usr/local/src/ghc-8.0.2/bin/ghc --make -fllvm -O2 -XBangPatterns -threaded -rtsopts -XScopedTypeVariables fannkuchredux.ghc-3.hs -o fannkuchredux.ghc-3.ghc_run
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./fannkuchredux.ghc-3.ghc_run +RTS -N4 -RTS 12

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./fannkuchredux.ghc-3.ghc_run +RTS -N4 -RTS 12

