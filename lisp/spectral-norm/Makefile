compile:
	sbcl --load spectralnorm.lisp --eval "(save-lisp-and-die \"spectralnorm.core\" :purify t :toplevel (lambda () (main) (quit)))"

measure:
	/opt/rapl/main "sbcl --noinform --core spectralnorm.core 5500" Lisp spectral-norm

run:
	sbcl --noinform --core spectralnorm.core 5500

clean:
	rm -rf *.core

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  sbcl --noinform --core spectralnorm.core 5500

valgrind:
	valgrind --tool=massif --stacks=yes  sbcl --noinform --core spectralnorm.core 5500
