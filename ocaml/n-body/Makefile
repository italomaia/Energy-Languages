compile:
	cp nbody.ocaml nbody.ml
	${COMPILER} -noassert -unsafe -fPIC -nodynlink -inline 100  nbody.ml -o nbody.ocaml_run
	rm nbody.ml
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./nbody.ocaml_run 50000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./nbody.ocaml_run 50000000

