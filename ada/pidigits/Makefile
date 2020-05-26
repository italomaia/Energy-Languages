compile:
	gnatchop -r -w pidigits.gnat-2.gnat
	gnatchop -r -w pidigits.gnat-2.gnat
	gnatmake -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp -f pidigits.adb -o pidigits.gnat-2.gnat_run
	gcc-6 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp pidigits.adb
	gnatbind-6 -x pidigits.ali
	gnatlink-6 pidigits.ali -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -o pidigits.gnat-2.gnat_run
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./pidigits.gnat-2.gnat_run 10000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./pidigits.gnat-2.gnat_run 10000

