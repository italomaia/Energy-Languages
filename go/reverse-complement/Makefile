compile:
	/usr/bin/go build -o revcomp.go-6.go_run

measure:
	/opt/rapl/main "./revcomp.go-6.go_run 0 < /root/data/revcomp-input25000000.txt" Go reverse-complement

run:
	./revcomp.go-6.go_run 0 < /root/data/revcomp-input25000000.txt

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v   ./revcomp.go-6.go_run 0 < /root/data/revcomp-input25000000.txt

valgrind:
	valgrind --tool=massif --stacks=yes   ./revcomp.go-6.go_run 0 < /root/data/revcomp-input25000000.txt
