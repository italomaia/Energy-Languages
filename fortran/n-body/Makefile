compile:
	ifort -O3 -fast nbody.ifc-6.f90 -o nbody.ifc-6.ifc_run
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./nbody.ifc-6.ifc_run 50000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./nbody.ifc-6.ifc_run 50000000

