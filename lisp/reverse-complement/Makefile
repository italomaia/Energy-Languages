compile:
	sbcl --load revcomp.lisp --eval "(save-lisp-and-die \"revcomp.core\" :purify t :toplevel (lambda () (main) (quit)))"

run:
	sbcl --noinform --core revcomp.core 0 < /root/data/revcomp-input25000000.txt

clean:
	rm -rf *.core

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  sbcl --noinform --core revcomp.core 0 < /root/data/revcomp-input25000000.txt

