compile:
	cp revcomp.java-3.java revcomp.java
	/usr/local/src/jdk1.8.0_121/bin/javac -d .  revcomp.java
run:
	/usr/local/src/jdk1.8.0_121/bin/java   revcomp 0 < /root/data/revcomp-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/jdk1.8.0_121/bin/java   revcomp 0 < /root/data/revcomp-input25000000.txt

