compile:

	cp binarytrees.jruby-5.jruby binarytrees.rb

prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/local/src/jruby-9.1.7.0/bin/jruby -Xcompile.fastest=true -Xcompile.invokedynamic=true -J-server -J-Xmx2G binarytrees.rb 21

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/jruby-9.1.7.0/bin/jruby -Xcompile.fastest=true -Xcompile.invokedynamic=true -J-server -J-Xmx2G binarytrees.rb 21

