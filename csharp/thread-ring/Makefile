compile:
	cp threadring.csharpcore Program.cs
	/usr/bin/dotnet build -c Release

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/bin/dotnet ./bin/Release/netcoreapp1.1/tmp.dll 50000000
