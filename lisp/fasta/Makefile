compile:
	sbcl --load fasta.lisp --eval "(save-lisp-and-die \"fasta.core\" :purify t :toplevel (lambda () (main) (quit)))"

run:
	sbcl --noinform --core fasta.core 25000000

clean:
	rm -rf *core

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v sbcl --noinform --core fasta.core 25000000

