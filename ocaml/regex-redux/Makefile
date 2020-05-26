compile:
	cp regexredux.ocaml-2.ocaml regexredux.ocaml-2.ml
	${COMPILER} -noassert -unsafe -fPIC -nodynlink -inline 100 unix.cmxa str.cmxa regexredux.ocaml-2.ml -o regexredux.ocaml-2.ocaml_run
	rm regexredux.ocaml-2.ml
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./regexredux.ocaml-2.ocaml_run 0 < /root/data/regexredux-input5000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  /usr/bin/time -o /opt/measures/${TLANG}.txt -v  /usr/bin/time -o /opt/measures/${TLANG}.txt -v  ./regexredux.ocaml-2.ocaml_run 0 < /root/data/regexredux-input5000000.txt

