compile:
	ifort -O3 -xHost -qopenmp -static-intel -ip -lapr-1 binarytrees.ifc-2.f90 -o binarytrees.ifc-2.ifc_run

run:
	./binarytrees.ifc-2.ifc_run 21

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./binarytrees.ifc-2.ifc_run 21

