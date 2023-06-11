#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-11 20:34:15

# import argparse

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



def main():
    target, numbers = 319, [3, 5, 7, 8, 11, 20]
    solve(target, numbers)
    target, numbers = 414, [3, 4, 11, 17, 21, 24]
    solve(target, numbers)
    target, numbers = 6, [3, 4, 11, 21]
    solve(target, numbers)
    target, numbers = 84, [1,2,3,4,5,25]
    solve(target, numbers)
    target, numbers = 414, [3, 4, 11, 17, 21, 24] # 17*24+21-11-4

    solve(target, numbers)

if __name__ == '__main__':
    main()
