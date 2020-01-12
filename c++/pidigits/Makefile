compile:
	/usr/bin/g++ -c -pipe -O3 -fomit-frame-pointer -march=native  -std=c++14 -g pidigits.gpp-4.c++ -o pidigits.gpp-4.c++.o &&  /usr/bin/g++ pidigits.gpp-4.c++.o -o pidigits.gpp-4.gpp_run -lgmp -lgmpxx
run:
	./pidigits.gpp-4.gpp_run 10000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./pidigits.gpp-4.gpp_run 10000

