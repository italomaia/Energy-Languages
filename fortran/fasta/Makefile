compile:
	ifort -O3 -fast -opt-streaming-stores always fasta.ifc-4.f90 -o fasta.ifc-4.ifc_run
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./fasta.ifc-4.ifc_run 25000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./fasta.ifc-4.ifc_run 25000000

