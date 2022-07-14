run:
	./radixsort.py 170 45 75 90 2 802 2 66

run2:
	./radixsort2.py 170 45 75 90 2 802 2 66

test:
	python3 -m pytest -v radixsort.py

test2:
	python3 -m pytest -v radixsort2.py

1K:
	./gen_inputs.py > 1K.txt

100K:
	./gen_inputs.py -n 100000 > 100K.txt

1M:
	./gen_inputs.py -n 1000000 > 1M.txt

bench: 1K 100K
	./bench.sh
