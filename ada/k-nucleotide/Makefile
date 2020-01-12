compile:
	gnatchop -r -w knucleotide.gnat-2.gnat
	gnatmake -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp -f knucleotide.adb -o knucleotide.gnat-2.gnat_run
	gcc-6 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp knucleotide.adb
	gcc-6 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp data_input.adb
	gcc-6 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp string_fragments.adb
	gcc-6 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp line_io.adb
	gnatbind-6 -x knucleotide.ali
	gnatlink-6 knucleotide.ali -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -o knucleotide.gnat-2.gnat_run

run:
	./knucleotide.gnat-2.gnat_run 0 < /root/data/knucleotide-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./knucleotide.gnat-2.gnat_run 0 < /root/data/knucleotide-input25000000.txt

