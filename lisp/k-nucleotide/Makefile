compile:
	sbcl --load knucleotide.lisp --eval "(save-lisp-and-die \"knucleotide.core\" :purify t :toplevel (lambda () (main) (quit)))"

xmeasure:
	/opt/rapl/main "sbcl --noinform --core knucleotide.core 5500" Lisp k-nucleotide

run:
	sbcl --noinform --core knucleotide.core --userinit /dev/null --load knucleotide.sbcl-6.sbcl_run 0 < /root/data/knucleotide-input25000000.txt

clean:
	rm -rf *core

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  sbcl --noinform --core knucleotide.core --userinit /dev/null --load knucleotide.sbcl-6.sbcl_run 0 < /root/data/knucleotide-input25000000.txt

valgrind:
	valgrind --tool=massif --stacks=yes  sbcl --noinform --core knucleotide.core --userinit /dev/null --load knucleotide.sbcl-6.sbcl_run 0 < /root/data/knucleotide-input25000000.txt
