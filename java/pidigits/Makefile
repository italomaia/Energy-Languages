compile:
	cp pidigits.java-2.java pidigits.java
	/usr/local/src/jdk1.8.0_121/bin/javac -d .  pidigits.java
xprepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/local/src/jdk1.8.0_121/bin/java -Djava.library.path=Include/java  pidigits 10000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/jdk1.8.0_121/bin/java -Djava.library.path=Include/java  pidigits 10000


