compile:
	/usr/local/src/chapel-1.15.0/bin/linux64/chpl --fast pidigits.chapel-2.chpl -o pidigits.chapel-2.chapel_run
xprepare:
	mkdir -p /opt/results/${TLANG}
	mkdir -p /opt/measures/${TLANG}

run:
	./pidigits.chapel-2.chapel_run --n=10000

comp2:
	@+if [ "$(CHPL_MAKE_GMP)" != "none" ]; then \
	$(CHPL) -o $@ $(CHPL_FLAGS) $<; \
	else \
	echo "";\
	echo $(CHPL_MAKE_GMP) \
	echo "Can't build pidigits without CHPL_GMP being enabled. See for details:"; \
	echo "http://chapel.cray.com/docs/latest/usingchapel/chplenv.html#chpl-gmp"; \
	echo ""; \
	fi

measure:
	/usr/bin/time -o /opt/measures/${TLANG}.txt -v ./pidigits.chapel-2.chapel_run --n=10000

