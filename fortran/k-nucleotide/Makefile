compile:
	ifort -O3 -fast -openmp knucleotide.f90 -o knucleotide.ifc_run
run:
	./knucleotide.ifc_run 0 < /root/data/knucleotide-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./knucleotide.ifc_run 0 < /root/data/knucleotide-input25000000.txt

