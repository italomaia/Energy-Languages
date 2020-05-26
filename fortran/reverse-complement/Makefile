compile:
	ifort -O3 -fast revcomp.f90 -o revcomp.ifc_run
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./revcomp.ifc_run 0 < /root/data/revcomp-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./revcomp.ifc_run 0 < /root/data/revcomp-input25000000.txt

