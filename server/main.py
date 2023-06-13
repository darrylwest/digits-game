# from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class Problem(BaseModel):
    target: int
    numbers: list
    
app = FastAPI()

origins = [ "http://localhost", "http://localhost:9800", ]

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

    return {"result": "2432"}
