compile:
	ifort -O3 -fast -openmp fannkuchredux.ifc-3.f90 -o fannkuchredux.ifc-3.ifc_run
run:
	./fannkuchredux.ifc-3.ifc_run 12

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./fannkuchredux.ifc-3.ifc_run 12

