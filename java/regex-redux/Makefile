compile:
	cp regexredux.java-3.java regexredux.java
	/usr/local/src/jdk1.8.0_121/bin/javac -d .  regexredux.java
prepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	/usr/local/src/jdk1.8.0_121/bin/java   regexredux 0 < /root/data/regexredux-input5000000.txt

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v /usr/local/src/jdk1.8.0_121/bin/java   regexredux 0 < /root/data/regexredux-input5000000.txt

