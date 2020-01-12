compile:
	#sbcl --load regexredux.lisp --eval "(save-lisp-and-die \"regexredux.core\" :purify t :toplevel (lambda () (main) (quit)))"
	(echo "Unknown Error" >>/dev/stderr)
	exit 1

xmeasure:
	#/opt/rapl/main "sbcl --noinform --core regexredux.core < 0 < /root/data/regexredux-input5000000.txt" Lisp regex-redux

clean:
	rm -rf *core

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v regexredux.core < 0 < /root/data/regexredux-input5000000.txt Lisp regex-redux

