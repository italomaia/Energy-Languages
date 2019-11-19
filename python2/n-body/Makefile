compile:
	cp nbody.python3 nbody.py
measure:
	sudo modprobe msr
	sudo /opt/rapl/main "${BINARY} -OO nbody.py 50000000" Python n-body

run:
	${BINARY} -OO nbody.py 50000000

mem:
	/usr/bin/time -v ${BINARY} -OO nbody.py 50000000
