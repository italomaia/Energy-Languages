compile:
	ifort -O3 -fast -qopenmp spectralnorm.ifc-3.f90 -o spectralnorm.ifc-3.ifc_run
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./spectralnorm.ifc-3.ifc_run 5500

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./spectralnorm.ifc-3.ifc_run 5500


