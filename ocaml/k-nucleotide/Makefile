compile:
	cp knucleotide.ocaml-3.ocaml knucleotide.ocaml-3.ml
	${COMPILER} -noassert -unsafe -fPIC -nodynlink -inline 100 unix.cmxa knucleotide.ocaml-3.ml -o knucleotide.ocaml-3.ocaml_run
	rm knucleotide.ocaml-3.ml

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./knucleotide.ocaml-3.ocaml_run 0 < /root/data/knucleotide-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./knucleotide.ocaml-3.ocaml_run 0 < /root/data/knucleotide-input25000000.txt

