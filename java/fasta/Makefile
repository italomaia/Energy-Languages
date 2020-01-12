compile:
	cp fasta.java-5.java fasta.java
	/usr/local/src/jdk1.8.0_121/bin/javac -d .  fasta.java
run:
	/usr/local/src/jdk1.8.0_121/bin/java   fasta 25000000

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/jdk1.8.0_121/bin/java   fasta 25000000

