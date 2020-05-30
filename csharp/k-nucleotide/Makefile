compile:
	cp knucleotide.csharpcore-6.csharpcore Program.cs
	${BINARY} build -c Release

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	${BINARY} ./bin/Release/netcoreapp1.1/tmp.dll 0 < /root/data/knucleotide-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ${BINARY} ./bin/Release/netcoreapp1.1/tmp.dll 0 < /root/data/knucleotide-input25000000.txt

