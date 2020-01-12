compile:
	cp fasta.ocaml-6.ocaml fasta.ocaml-6.ml
	${COMPILER} -noassert -unsafe -fPIC -nodynlink -inline 100 unix.cmxa fasta.ocaml-6.ml -o fasta.ocaml-6.ocaml_run

run:
	./fasta.ocaml-6.ocaml_run 25000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./fasta.ocaml-6.ocaml_run 25000000

