compile:
	csc -o Program.cs

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} Program.exe 10000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  ${BINARY} Program.exe 10000

