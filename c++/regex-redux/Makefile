compile:
	/usr/bin/g++ -c -pipe -O3 -fomit-frame-pointer -march=native  -fopenmp regexredux.gpp-3.c++ -o regexredux.gpp-3.c++.o &&  /usr/bin/g++ regexredux.gpp-3.c++.o -o regexredux.gpp-3.gpp_run -fopenmp -lboost_regex
run:
	./regexredux.gpp-3.gpp_run 0 < /root/data/regexredux-input5000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./regexredux.gpp-3.gpp_run 0 < /root/data/regexredux-input5000000.txt

