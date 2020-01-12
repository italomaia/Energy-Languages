compile:
	ifort -O3 -fast -openmp fannkuchredux.ifc-3.f90 -o fannkuchredux.ifc-3.ifc_run
measure:
	/opt/rapl/main "./fannkuchredux.ifc-3.ifc_run 12" Fortran fannkuch-redux

run:
	./fannkuchredux.ifc-3.ifc_run 12

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./fannkuchredux.ifc-3.ifc_run 12

valgrind:
	valgrind --tool=massif --stacks=yes ./fannkuchredux.ifc-3.ifc_run 12
