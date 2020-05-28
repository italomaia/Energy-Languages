compile:
	cp nbody.ghc-2.ghc nbody.ghc-2.hs
	/usr/local/src/ghc-8.0.2/bin/ghc --make -fllvm -O2 -XBangPatterns -threaded -rtsopts  nbody.ghc-2.hs -o nbody.ghc-2.ghc_run
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./nbody.ghc-2.ghc_run +RTS -N4 -RTS 50000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./nbody.ghc-2.ghc_run +RTS -N4 -RTS 50000000

