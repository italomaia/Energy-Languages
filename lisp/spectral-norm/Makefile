compile:
	sbcl --load spectralnorm.lisp --eval "(save-lisp-and-die \"spectralnorm.core\" :purify t :toplevel (lambda () (main) (quit)))"

run:
	sbcl --noinform --core spectralnorm.core 5500

clean:
	rm -rf *.core

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  sbcl --noinform --core spectralnorm.core 5500

