compile:
	cp binarytrees.fpascal binarytrees.pas
	/usr/local/src/fpc-3.0.2.x86_64-linux/bin/fpc -FuInclude/fpascal -XXs -O4 -Tlinux  -oFPASCAL_RUN binarytrees.pas
	mv FPASCAL_RUN binarytrees.fpascal_run
	rm binarytrees.pas

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./binarytrees.fpascal_run 21

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./binarytrees.fpascal_run 21

