compile:
	cp revcomp.ocaml-3.ocaml revcomp.ocaml-3.ml
	${COMPILER} -noassert -unsafe -fPIC -nodynlink -inline 100 unix.cmxa revcomp.ocaml-3.ml -o revcomp.ocaml-3.ocaml_run
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./revcomp.ocaml-3.ocaml_run 0 < /root/data/revcomp-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./revcomp.ocaml-3.ocaml_run 0 < /root/data/revcomp-input25000000.txt

