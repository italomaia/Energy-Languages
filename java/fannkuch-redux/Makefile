compile:
	/usr/local/src/jdk1.8.0_121/bin/javac -d .  fannkuchredux.java
measure:
	/opt/rapl/main "/usr/local/src/jdk1.8.0_121/bin/java   fannkuchredux 12" Java fannkuch-redux

run:
	/usr/local/src/jdk1.8.0_121/bin/java   fannkuchredux 12

mem:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  /usr/local/src/jdk1.8.0_121/bin/java   fannkuchredux 12

valgrind:
	valgrind --tool=massif --stacks=yes  /usr/local/src/jdk1.8.0_121/bin/java   fannkuchredux 12
