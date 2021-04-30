compile:
	/usr/bin/g++ -c -pipe -O3 -fomit-frame-pointer -march=native -mfpmath=sse -msse3 -std=c++11 fasta.gpp-5.c++ -o fasta.gpp-5.c++.o &&  /usr/bin/g++ fasta.gpp-5.c++.o -o fasta.gpp-5.gpp_run -lpthread

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./fasta.gpp-5.gpp_run 25000000 > /opt/results/${TLANG}/${TEST_NAME}.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./fasta.gpp-5.gpp_run 25000000


