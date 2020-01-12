compile:
	cp revcomp.ghc-3.ghc revcomp.ghc-3.hs
	/usr/local/src/ghc-8.0.2/bin/ghc --make -fllvm -O2 -XBangPatterns -threaded -rtsopts -funfolding-use-threshold=32 -XMagicHash -XUnboxedTuples revcomp.ghc-3.hs -o revcomp.ghc-3.ghc_run
run:
	./revcomp.ghc-3.ghc_run +RTS -N4 -RTS 0 < /root/data/revcomp-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./revcomp.ghc-3.ghc_run +RTS -N4 -RTS 0 < /root/data/revcomp-input25000000.txt

