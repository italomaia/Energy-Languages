compile:
	gnatchop -r -w fasta.gnat-5.gnat
	gnatmake -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp -f fasta.adb -o fasta.gnat-5.gnat_run
	gcc-6 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp fasta.adb
	gcc-6 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp sequence.ads
	gcc-6 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp sequence-creation.adb
	gcc-6 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp sequence-data.ads
	gcc-6 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp lcg_random.adb
	gcc-6 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp line_io.adb
	gnatbind-6 -x fasta.ali
	gnatlink-6 fasta.ali -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -o fasta.gnat-5.gnat_run

run:
	./fasta.gnat-5.gnat_run 25000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./fasta.gnat-5.gnat_run 25000000

