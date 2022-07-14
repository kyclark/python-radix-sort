run: run1 run2 file1 file2

run1:
	./radixsort.py -v 170 45 75 90 2 802 2 66

run2:
	./radixsort2.py -v 170 45 75 90 2 802 2 66

file1: smol
	./radixsort.py -f 10.txt

file2: smol
	./radixsort2.py -f 10.txt

test: test1 test2

test1:
	python3 -m pytest -v radixsort.py

test2:
	python3 -m pytest -v radixsort2.py

smol:
	./gen_inputs.py -n 10 > 10.txt

1K:
	./gen_inputs.py > 1K.txt

100K:
	./gen_inputs.py -n 100000 > 100K.txt

1M:
	./gen_inputs.py -n 1000000 > 1M.txt

bench: 1K 100K
	./bench.sh
