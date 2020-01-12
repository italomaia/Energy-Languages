compile:
	gnatchop -r -w spectralnorm.gnat-4.gnat
	gnatmake -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp -f spectralnorm.adb -o spectralnorm.gnat-4.gnat_run
	gcc-6 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp spectralnorm.adb
	gcc-6 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp division.ads
	gcc-6 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp division-d.adb
	gcc-6 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp division-s.ads
	gcc-6 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp spectral_utils.adb
	gcc-6 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp spectral_utils-d.adb
	gcc-6 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp spectral_utils-dist.adb
	gcc-6 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp spectral_utils-s.adb
	gnatbind-6 -x spectralnorm.ali
	gnatlink-6 spectralnorm.ali -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -o spectralnorm.gnat-4.gnat_run

run:
	./spectralnorm.gnat-4.gnat_run 5500

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./spectralnorm.gnat-4.gnat_run 5500

