# from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from itertools import permutations, product
from config import Config

import logging as log
# from fastapi.logger import logger as log

log.basicConfig(level=log.INFO)

class Problem(BaseModel):
    target: int
    numbers: list
    
config = Config()

app = FastAPI(
        title="DigitsGameSolver",
        description="""Visit port 8088/docs for the API Documentation""",
        version="0.0.4"
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def home() -> dict:
    return {"message":"howdy fastapi with cors enabled."}

@app.post("/problems")
async def solve(problem: Problem) -> dict:
    # todo: add console logging
    # print(problem)
    log.info(problem)

    # todo: implement digit_solver()
    result = digit_solver(problem.target, problem.numbers)
    # print(result)
    log.info(result)

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
