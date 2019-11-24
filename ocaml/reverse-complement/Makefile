compile:
	cp revcomp.ocaml-3.ocaml revcomp.ocaml-3.ml
	${COMPILER} -noassert -unsafe -fPIC -nodynlink -inline 100 unix.cmxa revcomp.ocaml-3.ml -o revcomp.ocaml-3.ocaml_run
measure:
	/opt/rapl/main "./revcomp.ocaml-3.ocaml_run 0 < /root/data/revcomp-input25000000.txt" OCaml reverse-complement

run:
	./revcomp.ocaml-3.ocaml_run 0 < /root/data/revcomp-input25000000.txt

mem:
	/usr/bin/time -v  ./revcomp.ocaml-3.ocaml_run 0 < /root/data/revcomp-input25000000.txt

valgrind:
	valgrind --tool=massif --stacks=yes  ./revcomp.ocaml-3.ocaml_run 0 < /root/data/revcomp-input25000000.txt
