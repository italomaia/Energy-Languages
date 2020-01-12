compile:
	cp mandelbrot.java-2.java mandelbrot.java
	/usr/local/src/jdk1.8.0_121/bin/javac -d .  mandelbrot.java
run:
	/usr/local/src/jdk1.8.0_121/bin/java   mandelbrot 16000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/jdk1.8.0_121/bin/java   mandelbrot 16000

