compile:
	cp regexredux.jruby-2.jruby regexredux.rb

run:
	/usr/local/src/jruby-9.1.7.0/bin/jruby -Xcompile.fastest=true -Xcompile.invokedynamic=true -J-server -J-Xmn512m -J-Xms2048m -J-Xmx2048m regexredux.rb 0 < /root/data/regexredux-input5000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  /usr/local/src/jruby-9.1.7.0/bin/jruby -Xcompile.fastest=true -Xcompile.invokedynamic=true -J-server -J-Xmn512m -J-Xms2048m -J-Xmx2048m regexredux.rb 0 < /root/data/regexredux-input5000000.txt

