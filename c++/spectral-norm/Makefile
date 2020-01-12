compile:
	/usr/bin/g++ -c -pipe -O3 -fomit-frame-pointer -march=native -mfpmath=sse -msse2 -fopenmp -mfpmath=sse -msse2 spectralnorm.gpp-6.c++ -o spectralnorm.gpp-6.c++.o &&  /usr/bin/g++ spectralnorm.gpp-6.c++.o -o spectralnorm.gpp-6.gpp_run -fopenmp
run:
	./spectralnorm.gpp-6.gpp_run 5500

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./spectralnorm.gpp-6.gpp_run 5500

