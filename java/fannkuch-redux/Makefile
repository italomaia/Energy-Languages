compile:
	/usr/local/src/jdk1.8.0_121/bin/javac -d .  fannkuchredux.java
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/local/src/jdk1.8.0_121/bin/java   fannkuchredux 12

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  /usr/local/src/jdk1.8.0_121/bin/java   fannkuchredux 12

