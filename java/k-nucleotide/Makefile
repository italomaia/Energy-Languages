compile:
	/usr/local/src/jdk1.8.0_121/bin/javac -d . -cp .:/usr/local/src/java-libs/fastutil-7.0.12.jar knucleotide.java
run:
	/usr/local/src/jdk1.8.0_121/bin/java  -cp .:/usr/local/src/java-libs/fastutil-7.0.12.jar knucleotide 0 < /root/data/knucleotide-input25000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v  /usr/local/src/jdk1.8.0_121/bin/java  -cp .:/usr/local/src/java-libs/fastutil-7.0.12.jar knucleotide 0 < /root/data/knucleotide-input25000000.txt

