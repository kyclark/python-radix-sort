run:
	./radixsort.py 170 45 75 90 2 802 2 66

run2:
	./radixsort2.py 170 45 75 90 2 802 2 66

test:
	python3 -m pytest -v radixsort.py

test2:
	python3 -m pytest -v radixsort2.py
