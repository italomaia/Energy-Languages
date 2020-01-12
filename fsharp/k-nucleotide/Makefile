compile:
	cp knucleotide.fsharpcore-4.fsharpcore Program.fs
	/usr/bin/dotnet build -c Release

run:
	/usr/bin/dotnet ./bin/Release/netcoreapp1.1/tmp.dll 0 < /root/data/knucleotide-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  /usr/bin/dotnet ./bin/Release/netcoreapp1.1/tmp.dll 0 < /root/data/knucleotide-input25000000.txt

