compile:
	cp spectralnorm.jruby-4.jruby spectralnorm.rb

run:
	/usr/local/src/jruby-9.1.7.0/bin/jruby -Xcompile.fastest=true -Xcompile.invokedynamic=true -J-server -J-Xmn512m -J-Xms2048m -J-Xmx2048m spectralnorm.rb 5500

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/jruby-9.1.7.0/bin/jruby -Xcompile.fastest=true -Xcompile.invokedynamic=true -J-server -J-Xmn512m -J-Xms2048m -J-Xmx2048m spectralnorm.rb 5500

