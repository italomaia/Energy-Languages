compile:
	cp nbody.jruby-2.jruby nbody.rb

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/local/src/jruby-9.1.7.0/bin/jruby -Xcompile.fastest=true -Xcompile.invokedynamic=true -J-server -J-Xmn512m -J-Xms2048m -J-Xmx2048m nbody.rb 50000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/jruby-9.1.7.0/bin/jruby -Xcompile.fastest=true -Xcompile.invokedynamic=true -J-server -J-Xmn512m -J-Xms2048m -J-Xmx2048m nbody.rb 50000000

