compile:
	cp fasta.ghc-2.ghc fasta.ghc-2.hs
	/usr/local/src/ghc-8.0.2/bin/ghc --make -fllvm -O2 -XBangPatterns -threaded -rtsopts -XOverloadedStrings fasta.ghc-2.hs -o fasta.ghc-2.ghc_run
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./fasta.ghc-2.ghc_run +RTS -N4 -RTS 25000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./fasta.ghc-2.ghc_run +RTS -N4 -RTS 25000000

