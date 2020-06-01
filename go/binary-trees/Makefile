compile:
	CGO_ENABLED=0 ${COMPILER} build binarytrees.go

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./binarytrees 21

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./binarytrees 21

