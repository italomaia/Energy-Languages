compile:
	sbcl --load fannkuch.lisp --eval "(save-lisp-and-die \"fannkuch.core\" :purify t :toplevel (lambda () (main) (quit)))"

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	sbcl --noinform --core fannkuch.core 12

clean:
	rm -rf *core

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v sbcl --noinform --core fannkuch.core 12



