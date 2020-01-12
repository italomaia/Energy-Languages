compile:
	cp regexredux.fsharpcore-2.fsharpcore Program.fs
	/usr/bin/dotnet build -c Release

measure:
	/opt/rapl/main "/usr/bin/dotnet ./bin/Release/netcoreapp1.1/tmp.dll 0 < /root/data/regexredux-input5000000.txt" FSharp regex-redux

run:
	/usr/bin/dotnet ./bin/Release/netcoreapp1.1/tmp.dll 0 < /root/data/regexredux-input5000000.txt

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/bin/dotnet ./bin/Release/netcoreapp1.1/tmp.dll 0 < /root/data/regexredux-input5000000.txt

valgrind:
	valgrind --tool=massif --stacks=yes /usr/bin/dotnet ./bin/Release/netcoreapp1.1/tmp.dll 0 < /root/data/regexredux-input5000000.txt
