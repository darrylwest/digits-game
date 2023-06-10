#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-10 12:35:40

# import numpy as np
# import argparse

# parse the target and array of variables

def sums(target, lst, idx, jdx):
    while  True:
        j = target - (sum(lst) - lst[jdx])
        lst[5] = j
        if (lst[idx] >= lst[jdx]):
            break

        print(target, lst, sum(lst))
        lst[idx] = lst[idx] + 1

def brute_force(target):
    print(f'brute force: {target}')

    n = 5
    idx = 4
    jdx = 5

    while True:
        lst = [1,2,3,n,n+1,0]
        sums(target, lst[:], idx, jdx)

        n = n + 1
        lst[idx] = lst[idx] + 1
        lst[jdx] = n + 2

        if (sum(lst) >= target):
            break


def main():
    brute_force(100)

if __name__ == '__main__':
    main()
