compile:
	/usr/bin/g++ -c -pipe -O3 -fomit-frame-pointer -march=native  -std=c++14 -fopenmp -I/usr/include/apr-1.0 binarytrees.gpp-9.c++ -o binarytrees.gpp-9.c++.o &&  /usr/bin/g++ binarytrees.gpp-9.c++.o -o binarytrees.gpp-9.gpp_run -fopenmp -lapr-1

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./binarytrees.gpp-9.gpp_run 21

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./binarytrees.gpp-9.gpp_run 21

