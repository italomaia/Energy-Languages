compile:
	/usr/bin/g++ -c -pipe -O3 -fomit-frame-pointer -march=native  -std=c++14 knucleotide.gpp-3.c++ -o knucleotide.gpp-3.c++.o &&  /usr/bin/g++ knucleotide.gpp-3.c++.o -o knucleotide.gpp-3.gpp_run -Wl,--no-as-needed -lpthread
run:
	./knucleotide.gpp-3.gpp_run 0 < /root/data/knucleotide-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./knucleotide.gpp-3.gpp_run 0 < /root/data/knucleotide-input25000000.txt

