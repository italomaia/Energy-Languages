compile:
	cp knucleotide.fsharpcore-4.fsharpcore Program.fs
	/usr/bin/dotnet build -c Release

measure:
	/opt/rapl/main "/usr/bin/dotnet ./bin/Release/netcoreapp1.1/tmp.dll 0 < /root/data/knucleotide-input25000000.txt" FSharp k-nucleotide

run:
	/usr/bin/dotnet ./bin/Release/netcoreapp1.1/tmp.dll 0 < /root/data/knucleotide-input25000000.txt

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  /usr/bin/dotnet ./bin/Release/netcoreapp1.1/tmp.dll 0 < /root/data/knucleotide-input25000000.txt

valgrind:
	valgrind --tool=massif --stacks=yes  /usr/bin/dotnet ./bin/Release/netcoreapp1.1/tmp.dll 0 < /root/data/knucleotide-input25000000.txt
