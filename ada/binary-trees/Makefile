compile:
	gnatchop -r -w binarytrees.gnat-4.gnat
	gnatmake -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp -f binarytrees.adb -o binarytrees.gnat-4.gnat_run -largs -lapr-1
	gcc -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp binarytrees.adb
	gcc -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp trees.adb
	gcc -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp apache_runtime.ads
	gcc -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp apache_runtime-pools.adb
	gnatbind -x binarytrees.ali
	gnatlink binarytrees.ali -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -o binarytrees.gnat-4.gnat_run -lapr-1
	chmod a+x /root/${TEST_NAME}/*.gnat_run

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./binarytrees.gnat-4.gnat_run 21

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./binarytrees.gnat-4.gnat_run 21

