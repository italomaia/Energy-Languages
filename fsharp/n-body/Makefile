compile:
	cp nbody.fsharpcore Program.fs
	/usr/bin/dotnet build -c Release

run:
	/usr/bin/dotnet ./bin/Release/netcoreapp1.1/tmp.dll 50000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/bin/dotnet ./bin/Release/netcoreapp1.1/tmp.dll 50000000

