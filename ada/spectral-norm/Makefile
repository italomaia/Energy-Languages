compile:
	gnatchop -r -w spectralnorm.gnat-4.gnat
	gnatmake -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp -f spectralnorm.adb -o spectralnorm.gnat-4.gnat_run
	gcc -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp spectralnorm.adb
	gcc -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp division.ads
	gcc -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp division-d.adb
	gcc -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp division-s.ads
	gcc -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp spectral_utils.adb
	gcc -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp spectral_utils-d.adb
	gcc -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp spectral_utils-dist.adb
	gcc -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp spectral_utils-s.adb
	gnatbind -x spectralnorm.ali
	gnatlink spectralnorm.ali -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -o spectralnorm.gnat-4.gnat_run
    chmod a+x /root/${TEST_NAME}/*.gnat_run

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./spectralnorm.gnat-4.gnat_run 5500

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./spectralnorm.gnat-4.gnat_run 5500

