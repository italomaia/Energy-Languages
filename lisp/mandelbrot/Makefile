compile:
	sbcl --load mandelbrot.lisp --eval "(save-lisp-and-die \"mandelbrot.core\" :purify t :toplevel (lambda () (main) (quit)))"

measure:
	/opt/rapl/main "sbcl --noinform --core mandelbrot.core 16000" Lisp mandelbrot

run:
	sbcl --noinform --core mandelbrot.core 16000

clean:
	rm -rf *core

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v sbcl --noinform --core mandelbrot.core 16000

valgrind:
	valgrind --tool=massif --stacks=yes sbcl --noinform --core mandelbrot.core 16000
