#!/usr/bin/env bash

hyperfine -m 100 -L prg ./radixsort.py,./radixsort2.py '{prg} -f 100K.txt' \
    --prepare 'rm -rf __pycache__'
