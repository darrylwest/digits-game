#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-11 18:16:47

# import numpy as np
# import sympy as sym
# import argparse

# use the small size array of integers to solve for the target using add/sub/mult/divide
def get_sums(target, numbers):
    s = sum(numbers)
    if (target == sum):
        print("found!")
        print(target, numbers, s, target - s)
        return s
    else:
        print(target, numbers, s, target - s)
        return s

def all_sums(target, numbers):
    original = numbers[:]

    for i in range(len(numbers)):
        numbers = original[:]
        numbers[i] = 0
        get_sums(6, numbers)
        rotate_zero(target, numbers)

def rotate_zero(target, numbers):
    original = numbers[:]

    for i in range(len(numbers)):
        numbers[i] = numbers[i] * -1
        get_sums(6, numbers)


def solve(target, numbers):
    original = [3, 4, 11, 21]

    print("add/subtract")
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * -1
        get_sums(6, numbers)

    all_sums(target, numbers)

def main():
    target = 6
    numbers = [3, 4, 11, 21]

    solve(target, numbers)


if __name__ == '__main__':
    main()
