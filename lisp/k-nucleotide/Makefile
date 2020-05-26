compile:
	sbcl --load knucleotide.lisp --eval "(save-lisp-and-die \"knucleotide.core\" :purify t :toplevel (lambda () (main) (quit)))"

xprepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	sbcl --noinform --core knucleotide.core --userinit /dev/null --load knucleotide.sbcl-6.sbcl_run 0 < /root/data/knucleotide-input25000000.txt

clean:
	rm -rf *core

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  sbcl --noinform --core knucleotide.core --userinit /dev/null --load knucleotide.sbcl-6.sbcl_run 0 < /root/data/knucleotide-input25000000.txt

