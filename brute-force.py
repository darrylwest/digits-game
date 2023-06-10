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
    lst = [1,2,3,4,5,85]
    idx = 4
    jdx = 5
    sums(target, lst, idx, jdx)


def main():
    brute_force(100)

if __name__ == '__main__':
    main()
