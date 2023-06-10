#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-10 18:46:56

# import numpy as np
# import sympy as sym
# import argparse

from collections import namedtuple

Pair = namedtuple('Pair', 'a b')
Factors = namedtuple('Factors', 'target pairs')
Game = namedtuple('Game', 'target numbers factors')

def factor(target):
    pairs = []

    for n in range(10):
        pair = Pair(n, n*n)
        pairs.append(pair)

    factors = Factors(target, pairs)

    return factors

def parse_args():
    game = Game(271, [3,4,6,7,8,11], None)
    print(f'game: {game}')

    return game
    
def main():
    # parse to get the startup game
    game = parse_args()

    factors = factor(game.target)
    print(f'factors: {factors}')

if __name__ == '__main__':
    main()
