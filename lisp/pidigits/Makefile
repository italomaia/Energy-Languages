compile:
	sbcl --load pidigits.lisp --eval "(save-lisp-and-die \"pidigits.core\" :purify t :toplevel (lambda () (main) (quit)))"

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	sbcl --noinform --core pidigits.core 10000

clean:
	rm -rf *core

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v sbcl --noinform --core pidbits.core 10000

