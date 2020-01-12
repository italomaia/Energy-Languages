compile:
	sbcl --load mandelbrot.lisp --eval "(save-lisp-and-die \"mandelbrot.core\" :purify t :toplevel (lambda () (main) (quit)))"

run:
	sbcl --noinform --core mandelbrot.core 16000

clean:
	rm -rf *core

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v sbcl --noinform --core mandelbrot.core 16000

