compile:
	gnatchop -r -w pidigits.gnat-2.gnat
	gnatchop -r -w pidigits.gnat-2.gnat
	gnatmake -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp -f pidigits.adb -o pidigits.gnat-2.gnat_run
	gcc -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp pidigits.adb
	gnatbind -x pidigits.ali
	gnatlink pidigits.ali -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -o pidigits.gnat-2.gnat_run
	chmod a+x /root/${TEST_NAME}/*.gnat_run

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./pidigits.gnat-2.gnat_run 10000 > /opt/results/${TLANG}/${TEST_NAME}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./pidigits.gnat-2.gnat_run 10000

