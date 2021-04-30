compile:
	gnatchop -r -w revcomp.gnat-2.gnat
	gnatmake -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp -f revcomp.adb -o revcomp.gnat-2.gnat_run
	gcc -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp revcomp.adb
	gcc -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp line_io.adb
	gcc -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp text_input.adb
	gnatbind -x revcomp.ali
	gnatlink revcomp.ali -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -o revcomp.gnat-2.gnat_run
	chmod a+x /root/${TEST_NAME}/*.gnat_run

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./revcomp.gnat-2.gnat_run 0 < /root/data/revcomp-input25000000.txt > /opt/results/${TLANG}/${TEST_NAME}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./revcomp.gnat-2.gnat_run 0 < /root/data/revcomp-input25000000.txt

