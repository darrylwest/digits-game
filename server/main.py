# from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from itertools import permutations, product

class Problem(BaseModel):
    target: int
    numbers: list
    
app = FastAPI()

# todo: read this from config file
origins = [ 
    "http://localhost",
    "http://localhost:9800",
    "http://plaza.local",
    "http://plaza.local:9800",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return {"message":"howdy fastapi with cors enabled?"}

@app.post("/problems")
async def solve(problem: Problem):
    # todo: add console logging
    print(problem)

    # todo: implement digit_solver()
    result = digit_solver(problem.target, problem.numbers)
    print(result)

    return {"result": result}

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

def digit_solver(target, numbers):
    result = find_operations(numbers, target)
    if result:
        return(f"{result} = {target}")
    else:
        return(f"No combination of operations found for {numbers} to equal {target}")
