compile:
	/usr/bin/g++ -c -pipe -O3 -fomit-frame-pointer -march=native  -std=c++11 -fopenmp fannkuchredux.gpp-5.c++ -o fannkuchredux.gpp-5.c++.o &&  /usr/bin/g++ fannkuchredux.gpp-5.c++.o -o fannkuchredux.gpp-5.gpp_run -fopenmp
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./fannkuchredux.gpp-5.gpp_run 12

measure:
	 /usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./fannkuchredux.gpp-5.gpp_run 12

