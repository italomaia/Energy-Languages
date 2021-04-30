compile:
	/usr/bin/g++ -c -pipe -O3 -fomit-frame-pointer -march=native -mfpmath=sse -msse3 --std=c++11 nbody.gpp-8.c++ -o nbody.gpp-8.c++.o &&  /usr/bin/g++ nbody.gpp-8.c++.o -o nbody.gpp-8.gpp_run -fopenmp

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./nbody.gpp-8.gpp_run 50000000 > /opt/results/${TLANG}/${TEST_NAME}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./nbody.gpp-8.gpp_run 50000000



