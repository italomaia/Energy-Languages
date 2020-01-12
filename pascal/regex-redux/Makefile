compile:
	cp regexredux.fpascal-2.fpascal regexredux.fpascal-2.pas
	/usr/local/src/fpc-3.0.2.x86_64-linux/bin/fpc -FuInclude/fpascal -XXs -O4 -Tlinux -oFPASCAL_RUN regexredux.fpascal-2.pas
	mv FPASCAL_RUN regexredux.fpascal-2.fpascal_run
	rm regexredux.fpascal-2.pas
run:
	./regexredux.fpascal-2.fpascal_run 0 < /root/data/regexredux-input5000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./regexredux.fpascal-2.fpascal_run 0 < /root/data/regexredux-input5000000.txt

