compile:

xmeasure:
	/opt/rapl/main "" TypeScript pidigits

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./binarytrees.gpp-9.gpp_run 21

valgrind:
	valgrind --tool=massif --stacks=yes ./binarytrees.gpp-9.gpp_run 21
