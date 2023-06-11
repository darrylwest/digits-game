#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-10 18:46:56

# import numpy as np
# import sympy as sym
# import argparse

from collections import namedtuple

Pair = namedtuple('Pair', 'a b')
Factors = namedtuple('Factors', 'target pairs')
Game = namedtuple('Game', 'target digits factors')

def parse_args():
    # game = Game(76, [1,2,3,4,10,25], [])
    # game = Game(131, [2,3,7,9,11,25], [])
    # game = Game(271, [3,4,6,7,8,11], [])
    # game = Game(312, [4,7,8,9,14,20], [])
    # game = Game(493, [9,11,14,21,23,25], [])

    # game = Game(55, [2,3,7,9,10,15], [])
    # game = Game(137, [2,3,7,9,10,15], [])
    # game = Game(291, [3,7,8,11,15,25], [])
    # game = Game(315, [3,7,8,9,11,25], [])
    # game = Game(453, [8,12,13,15,20,23], [])

    # game = Game(84, [1,2,3,4,5,25], [])
    # game = Game(134, [2,5,7,9,11,25], [])
    # game = Game(243, [7,8,11,15,20,25], [])
    # game = Game(319, [3,5,7,8,11,20], []) # needed to multioly by 3 terms first
    game = Game(414, [3,4,11,17,21,24], [])

    return game
    
def factor(target):
    pairs = []

    x = 2
    while (x < target):
        if (target % x == 0):
            pair = Pair(x, target // x)
            
            if (pair.a <= pair.b):
                pairs.append(pair)

        x = x + 1

    factors = Factors(target, pairs)

    return factors

def show_pairs(pairs):
    lst = []
    for p in pairs:
        lst.append(f'{p.a} * {p.b}')

    return lst
        

def show_factors(target, digits, factors):
    n = target - factors.target
    digits = [x for x in digits if x != abs(n) ]
    print(target, factors.target, n, digits)
    for pair in factors.pairs:
        if (pair.a in digits):
            lst = show_pairs(factor(pair.b).pairs)
            print(f"+ {pair.a} * {pair.b}", lst)
        elif (pair.b in digits):
            print(f"  {pair.a} * {pair.b} +")
        else:
            print(f"  {pair.a} * {pair.b}")


def show_game(game):
    print(f'Digits: {game.target}: {game.digits}' )
    for f in game.factors:
        show_factors(game.target, game.digits, f)
    
def main():
    # parse to get the startup game
    game = parse_args()

    for n in game.digits:
        game.factors.append(factor(game.target + n))
        game.factors.append(factor(game.target - n))

    show_game(game)

    print("\nlargest factors -------------")
    v = game.digits[:].pop()
    for n in game.digits[:5]:
        p = n*v
        r = game.target - p
        nums = [x for x in game.digits if x not in [v, n] ]
        # try to resolve an answer from the nums list; num, sum, prod
        # first find an r in the list
        q = [x for x in game.digits if x == r]
        # find a+n sum = r
        # find a*n prod = r


        print(f"{n} * {v} = {p} {r} {nums} : {q}")
        

if __name__ == '__main__':
    main()
