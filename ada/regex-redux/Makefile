compile:
	gnatchop -r -w regexredux.gnat-5.gnat
	gnatmake -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp -f regexredux.adb -o regexredux.gnat-5.gnat_run
	gcc-6 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp regexredux.adb
	gcc-6 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp block_input.adb
	gcc-6 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp dna.ads
	gcc-6 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp dna-matching.adb
	gcc-6 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp dna-replacing.adb
	gcc-6 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp preprocessing.adb
	gcc-6 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp u.ads
	gnatbind-6 -x regexredux.ali
	gnatlink-6 regexredux.ali -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -o regexredux.gnat-5.gnat_run
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./regexredux.gnat-5.gnat_run 0 < /root/data/regexredux-input5000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./regexredux.gnat-5.gnat_run 0 < /root/data/regexredux-input5000000.txt

