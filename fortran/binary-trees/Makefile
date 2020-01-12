compile:
	ifort -O3 -xHost -qopenmp -static-intel -ip -lapr-1 binarytrees.ifc-2.f90 -o binarytrees.ifc-2.ifc_run

measure:
	/opt/rapl/main "./binarytrees.ifc-2.ifc_run 21" Fortran binary-trees

run:
	./binarytrees.ifc-2.ifc_run 21

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./binarytrees.ifc-2.ifc_run 21

valgrind:
	valgrind --tool=massif --stacks=yes  ./binarytrees.ifc-2.ifc_run 21
