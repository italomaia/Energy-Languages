compile:

measure:
	/opt/rapl/main "/usr/bin/dart  binarytrees.dart 21" Dart binary-trees

run:
	/usr/bin/dart  binarytrees.dart 21

mem:
	/usr/bin/time -v  /usr/bin/dart  binarytrees.dart 21

valgrind:
	valgrind --tool=massif --stacks=yes  /usr/bin/dart  binarytrees.dart 21
