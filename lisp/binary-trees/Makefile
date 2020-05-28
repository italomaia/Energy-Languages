compile:
	sbcl --load binarytrees.lisp --eval "(save-lisp-and-die \"binarytrees.core\" :purify t :toplevel (lambda () (main) (quit)))"

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	sbcl --noinform --core binarytrees.core 21

clean:
	rm -rf *.core

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v sbcl --noinform --core binarytrees.core 21

