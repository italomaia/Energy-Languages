compile:
	cp mandelbrot.fsharpcore-3.fsharpcore Program.fs
	/usr/bin/dotnet build -c Release

measure:
	/opt/rapl/main "/usr/bin/dotnet ./bin/Release/netcoreapp1.1/tmp.dll 16000" FSharp mandelbrot

run:
	/usr/bin/dotnet ./bin/Release/netcoreapp1.1/tmp.dll 16000

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  /usr/bin/dotnet ./bin/Release/netcoreapp1.1/tmp.dll 16000

valgrind:
	valgrind --tool=massif --stacks=yes  /usr/bin/dotnet ./bin/Release/netcoreapp1.1/tmp.dll 16000
