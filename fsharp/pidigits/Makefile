compile:
	cp pidigits.fsharpcore-3.fsharpcore Program.fs
	/usr/bin/dotnet build -c Release

run:
	/usr/bin/dotnet ./bin/Release/netcoreapp1.1/tmp.dll 10000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/bin/dotnet ./bin/Release/netcoreapp1.1/tmp.dll 10000

