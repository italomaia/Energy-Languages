compile:
	cp spectralnorm.ocaml-3.ocaml spectralnorm.ocaml-3.ml
	${COMPILER} -noassert -unsafe -fPIC -nodynlink -inline 100 unix.cmxa bigarray.cmxa spectralnorm.ocaml-3.ml -o spectralnorm.ocaml-3.ocaml_run
	rm spectralnorm.ocaml-3.ml

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./spectralnorm.ocaml-3.ocaml_run 5500

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./spectralnorm.ocaml-3.ocaml_run 5500

