compile:
	ifort -O3 -xHost -ipo -lgmp pidigits.ifc-3.f90 -o pidigits.ifc-3.ifc_run
xrun:
	./pidigits.ifc-3.ifc_run 10000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./pidigits.ifc-3.ifc_run 10000

