compile:
	cp nbody.java-4.java nbody.java
	/usr/local/src/jdk1.8.0_121/bin/javac -d .  nbody.java
run:
	/usr/local/src/jdk1.8.0_121/bin/java   nbody 50000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/jdk1.8.0_121/bin/java   nbody 50000000

