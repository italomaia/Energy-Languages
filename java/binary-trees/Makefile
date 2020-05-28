compile:
	cp binarytrees.java-7.java binarytrees.java
	/usr/local/src/jdk1.8.0_121/bin/javac -d .  binarytrees.java
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/local/src/jdk1.8.0_121/bin/java binarytrees 21

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/jdk1.8.0_121/bin/java binarytrees 21

