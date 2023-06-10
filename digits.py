#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-10 18:46:56

# import numpy as np
# import sympy as sym
# import argparse

from collections import namedtuple

Pair = namedtuple('Pair', 'a b')
Factors = namedtuple('Factors', 'target pairs')

def factor(target):
    pairs = []

    for n in range(10):
        pair = Pair(n, n*n)
        pairs.append(pair)

    factors = Factors(target, pairs)

    return factors

def main():
    factors = factor(128)
    print(f'factors: {factors}')

if __name__ == '__main__':
    main()
