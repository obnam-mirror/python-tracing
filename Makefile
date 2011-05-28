all:
	$(MAKE) -C doc html

clean:
	$(MAKE) -C doc clean
	rm -rf build *.py[co]

