compile:
	cp fannkuchredux.csharpcore-4.csharpcore Program.cs
	/usr/bin/dotnet build -c Release

measure:
	/opt/rapl/main "/usr/bin/dotnet ./bin/Release/netcoreapp1.1/tmp.dll 12" CSharp fannkuch-redux

run:
	/usr/bin/dotnet ./bin/Release/netcoreapp1.1/tmp.dll 12

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  /usr/bin/dotnet ./bin/Release/netcoreapp1.1/tmp.dll 12

valgrind:
	valgrind --tool=massif --stacks=yes  /usr/bin/dotnet ./bin/Release/netcoreapp1.1/tmp.dll 12
