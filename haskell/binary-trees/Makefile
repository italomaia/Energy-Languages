compile:
	cp binarytrees.ghc binarytrees.hs
	/usr/local/src/ghc-8.0.2/bin/ghc --make -fllvm -O2 -XBangPatterns -threaded -rtsopts -funbox-strict-fields binarytrees.hs -o binarytrees.ghc_run

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./binarytrees.ghc_run +RTS -N4 -K128M -H -RTS 21

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./binarytrees.ghc_run +RTS -N4 -K128M -H -RTS 21

