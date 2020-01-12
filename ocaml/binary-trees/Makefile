compile:
	cp binarytrees.ocaml-2.ocaml binarytrees.ocaml-2.ml
	${COMPILER} -noassert -unsafe -fPIC -nodynlink -inline 100 unix.cmxa binarytrees.ocaml-2.ml -o binarytrees.ocaml-2.ocaml_run
	rm binarytrees.ocaml-2.ml

run:
	./binarytrees.ocaml-2.ocaml_run 21

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./binarytrees.ocaml-2.ocaml_run 21

