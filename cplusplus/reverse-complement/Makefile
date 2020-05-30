compile:
	/usr/bin/g++ -c -pipe -O3 -fomit-frame-pointer -march=native  -std=c++11 -mtune=native -mfpmath=sse -msse2 revcomp.gpp-4.c++ -o revcomp.gpp-4.c++.o &&  /usr/bin/g++ revcomp.gpp-4.c++.o -o revcomp.gpp-4.gpp_run -pthread
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./revcomp.gpp-4.gpp_run 0 < /root/data/revcomp-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./revcomp.gpp-4.gpp_run 0 < /root/data/revcomp-input25000000.txt

