compile:
	cp pidigits.ocaml-3.ocaml pidigits.ocaml-3.ml
	${COMPILER} -noassert -unsafe -fPIC -nodynlink -inline 100 -I /usr/local/lib/ocaml/gmp gmp.cmxa pidigits.ocaml-3.ml -o pidigits.ocaml-3.ocaml_run
	rm pidigits.ocaml-3.ml

xrun:
	./pidigits.ocaml-3.ocaml_run 2000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ../pidigits.ocaml-3.ocaml_run 2000

