compile:
	cp mandelbrot.csharpcore-5.csharpcore Program.cs
	/usr/bin/dotnet build -c Release

measure:
	/opt/rapl/main "/usr/bin/dotnet ./bin/Release/netcoreapp1.1/tmp.dll 16000" CSharp mandelbrot

run:
	/usr/bin/dotnet ./bin/Release/netcoreapp1.1/tmp.dll 16000

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/bin/dotnet ./bin/Release/netcoreapp1.1/tmp.dll 16000

valgrind:
	valgrind --tool=massif --stacks=yes /usr/bin/dotnet ./bin/Release/netcoreapp1.1/tmp.dll 16000
