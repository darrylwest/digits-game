#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-11 20:34:15

import argparse
from itertools import permutations, product

def find_operations(numbers, target):
    operations = ['+', '-', '*']
    for n in range(1, len(numbers)+1):
        for nums in permutations(numbers, n):
            for ops in product(operations, repeat=n-1):
                equation = f"{nums[0]}"
                for i in range(n-1):
                    equation += f"{ops[i]}{nums[i+1]}"
                if eval(equation) == target:
                    return equation
                equation = f"-{nums[0]}"
                for i in range(n-1):
                    equation += f"{ops[i]}{nums[i+1]}"
                if eval(equation) == target:
                    return equation
    return None

def solve(target, numbers):
    result = find_operations(numbers, target)
    if result:
        print(f"{result} = {target}")
    else:
        print(f"No combination of operations found for {numbers} to equal {target}")

def run_all():
    solve(76,[1,2,3,4,10,25])
    solve(131,[2,3,7,9,11,25])
    solve(271,[3,4,6,7,8,11])
    solve(312,[4,7,8,9,14,20])
    solve(493,[9,11,14,21,23,25])

    solve(55,[1,2,3,4,5,10])
    solve(137,[2,3,7,9,10,15])
    solve(291,[3,7,8,11,15,25])
    solve(315,[3,7,8,9,11,25])
    solve(453,[8,12,13,15,20,23])

    solve(6, [3, 4, 11, 21])

    solve(84, [1,2,3,4,5,25])
    solve(134,[2,5,7,9,11,25])
    solve(243,[7,8,11,15,20,25])
    solve(319, [3,5,7,8,11,20])
    solve(414, [3,4,11,17,21,24])

def main():
    # run_all()
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', type=int, required=True, help='the target number to solve for')
    parser.add_argument('-n', '--numbers', type=int, nargs='+', required=True, help='a list of integers to use in the solution')

    args = parser.parse_args()

    print(f"Target: {args.target}, numbers: {args.numbers}")
    solve(args.target, args.numbers)

if __name__ == '__main__':
    main()
