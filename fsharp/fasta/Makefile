compile:
	cp fasta.fsharpcore Program.fs
	/usr/bin/dotnet build -c Release

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/bin/dotnet ./bin/Release/netcoreapp1.1/tmp.dll 25000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/bin/dotnet ./bin/Release/netcoreapp1.1/tmp.dll 25000000

