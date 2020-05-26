compile:
	gnatchop -r -w fannkuchredux.gnat-3.gnat
	gnatmake -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp -f fannkuchredux.adb -o fannkuchredux.gnat-3.gnat_run
	gcc-6 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp fannkuchredux.adb
	gnatbind-6 -x fannkuchredux.ali
	gnatlink-6 fannkuchredux.ali -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -o fannkuchredux.gnat-3.gnat_run

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./fannkuchredux.gnat-3.gnat_run 12

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./fannkuchredux.gnat-3.gnat_run 12

