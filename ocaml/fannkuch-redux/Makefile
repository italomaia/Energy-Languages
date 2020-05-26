compile:
	cp fannkuchredux.ocaml-4.ocaml fannkuchredux.ocaml-4.ml
	${COMPILER} -noassert -unsafe -fPIC -nodynlink -inline 100 unix.cmxa fannkuchredux.ocaml-4.ml -o fannkuchredux.ocaml-4.ocaml_run
	rm fannkuchredux.ocaml-4.ml

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./fannkuchredux.ocaml-4.ocaml_run 12

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./fannkuchredux.ocaml-4.ocaml_run 12

