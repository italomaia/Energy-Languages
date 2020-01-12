compile:
	cp spectralnorm.ghc-4.ghc spectralnorm.ghc-4.hs
	/usr/local/src/ghc-8.0.2/bin/ghc --make -fllvm -O2 -XBangPatterns -threaded -rtsopts -XMagicHash spectralnorm.ghc-4.hs -o spectralnorm.ghc-4.ghc_run
run:
	./spectralnorm.ghc-4.ghc_run +RTS -N4 -RTS 5500

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./spectralnorm.ghc-4.ghc_run +RTS -N4 -RTS 5500

