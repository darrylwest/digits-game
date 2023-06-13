# from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [ "http://localhost", "http://localhost:3000", ]

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

# @app.post("/solve")
# async def solve(target: int, numbers: List[int] = Body()):
    # return {"result": "2432"}