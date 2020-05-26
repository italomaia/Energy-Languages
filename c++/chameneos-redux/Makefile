compile:
	/usr/bin/g++ -c -pipe -O3 -fomit-frame-pointer -march=native  --std=c++11 -pthread chameneosredux.gpp-5.c++ -o chameneosredux.gpp-5.c++.o && /usr/bin/g++ chameneosredux.gpp-5.c++.o -o chameneosredux.gpp-5.gpp_run -Wl,--no-as-needed -lpthread

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./chameneosredux.gpp-5.gpp_run 6000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./chameneosredux.gpp-5.gpp_run 6000000

