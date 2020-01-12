compile:
	/usr/bin/go build -o binarytrees.go-2.go_run

measure:
	/opt/rapl/main "./binarytrees.go-2.go_run 21" Go binary-trees

run:
	./binarytrees.go-2.go_run 21

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./binarytrees.go-2.go_run 21

valgrind:
	valgrind --tool=massif --stacks=yes ./binarytrees.go-2.go_run 21
