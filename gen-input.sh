#!/bin/bash

echo "Generating input for k-nucleotide benchmark"
/usr/bin/env python3 Python/fasta/fasta.python3-3.py 25000000 > knucleotide-input25000000.txt

echo "Generating input for reverse-complement benchmark"
/usr/bin/env python3 Python/fasta/fasta.python3-3.py 25000000 > revcomp-input25000000.txt

echo "Generating input for regex-redux benchmark"
/usr/bin/env python3 Python/fasta/fasta.python3-3.py 5000000 > regexredux-input5000000.txt