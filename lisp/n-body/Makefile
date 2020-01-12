compile:
	sbcl --load nbody.lisp --eval "(save-lisp-and-die \"nbody.core\" :purify t :toplevel (lambda () (main) (quit)))"

run:
	sbcl --noinform --core nbody.core 50000000

clean:
	rm -rf *core

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  sbcl --noinform --core nbody.core 50000000

